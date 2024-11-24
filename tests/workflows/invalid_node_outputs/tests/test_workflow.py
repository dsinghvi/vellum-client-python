from tests.workflows.invalid_node_outputs.workflow import InvalidNodeWorkflow
from vellum.workflows.errors.types import VellumErrorCode


def test_run_workflow__happy_path():
    # GIVEN a workflow that has an invalid node
    workflow = InvalidNodeWorkflow()

    # WHEN we run the workflow
    terminal_event = workflow.run()

    # THEN the workflow should have completed with a failure
    assert terminal_event.name == "workflow.execution.rejected", terminal_event

    # AND the outputs should be defaulted correctly
    assert terminal_event.error.code == VellumErrorCode.INVALID_OUTPUTS, terminal_event.error.message
    assert terminal_event.error.message == "Node InvalidNode did not return a valid node run response"