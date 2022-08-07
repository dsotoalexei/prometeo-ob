import { create } from '@storybook/theming';

const prometeoTheme = create({
  colorPrimary: 'black',
  colorSecondary: 'black',

  // UI
  appBg: 'white',
  appContentBg: 'white',
  appBorderColor: '#c24036',
  appBorderRadius: 4,

  // Typography
  fontBase: '"Open Sans", sans-serif',
  fontCode: 'monospace',

  // Text colors
  textColor: 'black',
  textInverseColor: 'rgba(255,255,255,0.9)',

  // Toolbar default and active colors
  barTextColor: 'white',
  barSelectedColor: 'black',
  barBg: '#f0291a',

  // Form colors
  inputBg: 'white',
  inputBorder: 'silver',
  inputTextColor: 'black',
  inputBorderRadius: 4,

  base: 'light',
  brandTitle: 'Prometeo Storybook',
  brandUrl: 'http://localhost:3000',
  brandImage: 'http://localhost:6006/assets/images/logo/logo.png',
  brandTarget: '_self',
});

export { prometeoTheme as default, prometeoTheme }
