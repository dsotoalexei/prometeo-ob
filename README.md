# prometeo-ob

**First we need to install the react-redux package**

```bash
$> npm install -E react-redux
$> npm install -DE @types/react-redux
```

**Then, install @reduxjs/toolkit package**

```bash
$> npm install -E @reduxjs/toolkit
```

**Install redux-logger package**

```bash
$> npm install -DE redux-logger @types/redux-logger
```

Install [Material UI](https://mui.com/)

```bash
$> npm install -E @mui/material @mui/styled-engine-sc @mui/icons-material
$> npm install -E react-helmet-async react-i18next styled-components
$> npm install -DE @types/styled-components
```

```bash
$> npx create-react-app my-app --template typescript
$> npx sb init

$> npx create-nx-workspace@latest client
$> npx nx g @nrwl/react:lib redux --directory=web --appProject=web
$> npm install -DE @nrwl/storybook
$> npx nx g @nrwl/react:storybook-configuration web-ui

// Generate with stories
$> npx nx g @nrwl/react:storybook-configuration web-ui --generateStories

// Generate with stories and cypress
$> npx nx g @nrwl/react:storybook-configuration web-ui --generateStories --configureCypress

// Run web
$> npx nx run web:serve

// Run storybook
$> npx nx run web-ui:storybook

// Run e2e test
$> npx nx run web-e2e:e2e --watch

// Run jest test
$> npx nx run web:test

// Run lint
$> npx nx run web:lint

// Build for production
$> npx nx run web:build --configuration=production
```