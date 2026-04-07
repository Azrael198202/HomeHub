declare module "react" {
  const React: any;
  export default React;
}

declare module "react-dom/client" {
  export function createRoot(container: Element | DocumentFragment): {
    render(node: unknown): void;
  };
}

declare namespace JSX {
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}
