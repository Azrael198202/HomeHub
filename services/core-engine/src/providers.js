import { modelProviders } from "../../packages/shared/src/demo-data.js";

export function listModelProviders() {
  return modelProviders;
}

export function resolveProviderByCapability(capability) {
  return modelProviders.filter((provider) => provider.capabilities.includes(capability));
}
