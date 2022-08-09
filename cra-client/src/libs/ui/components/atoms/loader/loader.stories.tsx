import { Story, Meta } from '@storybook/react';
import { Loader } from './loader';

export default {
  component: Loader,
  title: 'Atoms/Loader',
  parameters: {
    controls: { expanded: true },
  },
} as Meta;

const Template: Story<any> = (args) => <Loader {...args} />;

export const Default = Template.bind({});
Default.args = {};
