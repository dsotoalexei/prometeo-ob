module.exports = {
  stories: [
    {
      // 👇 The directory field sets the directory your stories
      directory: '../src/libs/ui/components',
      // 👇 The titlePrefix field will generate automatic titles for your stories
      // titlePrefix: 'MyComponents',
      // 👇 Storybook will load all files that contain the stories extension
      files: '*.stories.*',
    },
  ],
  addons: [
    '@storybook/addon-links',
    '@storybook/addon-essentials',
    '@storybook/addon-interactions',
    '@storybook/preset-create-react-app',
  ],
  framework: '@storybook/react',
  core: {
    builder: '@storybook/builder-webpack5',
  },
};
