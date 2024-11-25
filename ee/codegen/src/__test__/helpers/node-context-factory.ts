import { workflowContextFactory } from "./workflow-context-factory";

import { createNodeContext } from "src/context";
import { BaseNodeContext } from "src/context/node-context/base";
import {
  SearchNode,
  WorkflowDataNode,
  WorkflowNodeType as WorkflowNodeTypeEnum,
} from "src/types/vellum";

export function nodeContextFactory({
  workflowContext,
  nodeData,
}: Partial<
  BaseNodeContext.Args<WorkflowDataNode>
> = {}): BaseNodeContext<WorkflowDataNode> {
  return createNodeContext({
    workflowContext: workflowContext ?? workflowContextFactory(),
    nodeData: nodeData ?? {
      id: "search",
      type: WorkflowNodeTypeEnum.SEARCH,
      inputs: [],
      data: { label: "MyNode" } as SearchNode["data"],
    },
  });
}