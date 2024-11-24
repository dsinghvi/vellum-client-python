import pytest

from vellum.workflows.errors.types import VellumError, VellumErrorCode
from vellum.workflows.exceptions import NodeException
from vellum.workflows.inputs.base import BaseInputs
from vellum.workflows.nodes.bases import BaseNode
from vellum.workflows.nodes.core.try_node.node import TryNode
from vellum.workflows.outputs import BaseOutputs
from vellum.workflows.state.base import BaseState, StateMeta


def test_try_node__on_error_code__successfully_caught():
    # GIVEN a try node that is configured to catch PROVIDER_ERROR
    @TryNode.wrap(on_error_code=VellumErrorCode.PROVIDER_ERROR)
    class TestNode(BaseNode):
        class Outputs(BaseOutputs):
            value: int

        def run(self) -> Outputs:
            raise NodeException(message="This will be caught", code=VellumErrorCode.PROVIDER_ERROR)

    # WHEN the node is run and throws a PROVIDER_ERROR
    node = TestNode(state=BaseState())
    outputs = node.run()

    # THEN the exception is retried
    assert outputs == {
        "error": VellumError(message="This will be caught", code=VellumErrorCode.PROVIDER_ERROR),
    }


def test_try_node__retry_on_error_code__missed():
    # GIVEN a try node that is configured to catch PROVIDER_ERROR
    @TryNode.wrap(on_error_code=VellumErrorCode.PROVIDER_ERROR)
    class TestNode(BaseNode):
        class Outputs(BaseOutputs):
            value: int

        def run(self) -> Outputs:
            raise NodeException(message="This will be missed", code=VellumErrorCode.INTERNAL_ERROR)

    # WHEN the node is run and throws a different exception
    node = TestNode(state=BaseState())
    with pytest.raises(NodeException) as exc_info:
        node.run()

    # THEN the exception is not caught
    assert exc_info.value.message == "Unexpected rejection: INTERNAL_ERROR.\nMessage: This will be missed"
    assert exc_info.value.code == VellumErrorCode.INVALID_OUTPUTS


def test_try_node__use_parent_inputs_and_state():
    # GIVEN a parent workflow Inputs and State
    class Inputs(BaseInputs):
        foo: str

    class State(BaseState):
        bar: str

    # AND a try node that uses the parent's inputs and state
    @TryNode.wrap()
    class TestNode(BaseNode):
        foo = Inputs.foo
        bar = State.bar

        class Outputs(BaseOutputs):
            value: str

        def run(self) -> Outputs:
            return self.Outputs(value=f"{self.foo} {self.bar}")

    # WHEN the node is run
    node = TestNode(
        state=State(
            bar="bar",
            meta=StateMeta(workflow_inputs=Inputs(foo="foo")),
        ),
    )
    outputs = node.run()

    # THEN the data is used successfully
    assert outputs == {"value": "foo bar"}