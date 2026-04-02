import { skillCatalog } from "../../packages/shared/src/demo-data.js";

export function loadSkills() {
  return skillCatalog.map((descriptor) => ({
    descriptor,
    canHandle(inputMode) {
      return descriptor.inputModes.includes(inputMode);
    }
  }));
}
