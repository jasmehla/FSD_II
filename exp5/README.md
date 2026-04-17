# Optimize frontend performance using lazy loading

This repository demonstrates practical techniques to improve frontend performance in React + Vite projects by using lazy loading and related optimizations.

Key recommendations:

- Use code-splitting and dynamic imports (`React.lazy` + `Suspense`) for components and routes to reduce initial bundle size.
- Lazy-load images and media with `loading="lazy"` or the Intersection Observer API for better perceived performance.
- Defer or async non-critical scripts and consider preloading critical resources (`<link rel="preload">`).
- Analyze bundles with tools like `rollup-plugin-visualizer` or `source-map-explorer` and minimize large dependencies.
- Apply route-based chunking, component-level splitting, and optimize third-party libraries.
- Serve assets through a CDN, enable compression, and set long-term caching headers.

See [index.html](index.html) and the `src` directory for examples using dynamic imports and lazy-loaded components.

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).