import { Story, Meta } from '@storybook/react';
import { AccountCard } from './account-card';
import { IAccountCardProps } from './account-card.types';

export default {
  component: AccountCard,
  title: 'Atoms/Account Card',
  parameters: {
    controls: { expanded: true },
  },
} as Meta;

const Template: Story<IAccountCardProps> = (args) => <AccountCard {...args} />;

export const Default = Template.bind({});
Default.args = {
  name: 'Credit Card',
  number: '************1792',
  currency: '12/27/2022',
  balance: 25000,
};
