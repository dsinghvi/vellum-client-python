from vellum.workflows.nodes.bases import BaseNode


class MergeNode(BaseNode):
    """
    Used to merge the control flow of multiple nodes into a single node. This node exists to be backwards compatible
    with Vellum's Merge Node, and for most cases, you should extend from `BaseNode.Trigger` directly.
    """

    pass