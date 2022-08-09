import { Story, Meta } from '@storybook/react';
import { CreditCard } from './credit-card';
import { ICreditCardProps } from './credit-card.types';

export default {
  component: CreditCard,
  title: 'Atoms/Credit Card',
  parameters: {
    controls: { expanded: true },
  },
} as Meta;

const Template: Story<ICreditCardProps> = (args) => <CreditCard {...args} />;

export const Default = Template.bind({});
Default.args = {
  name: 'Credit Card',
  number: '************1792',
  close_date: '12/27/2022',
  due_date: '12/28/2022',
  balance_local: 25000,
  balance_dollar: 2500,
};
