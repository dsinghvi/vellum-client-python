import { BaseNodeContext } from "./base";

import { PortContext } from "src/context/port-context";
import { ErrorNode } from "src/types/vellum";

export class ErrorNodeContext extends BaseNodeContext<ErrorNode> {
  getNodeOutputNamesById(): Record<string, string> {
    return {};
  }

  createPortContexts(): PortContext[] {
    return [];
  }
}