import { render, screen } from '@testing-library/react';
import { Loader } from './loader';

test('renders loaders', () => {
  render(<Loader />);

  const elSvg = screen.getByTestId('loader-bar');
  expect(elSvg).toBeInTheDocument();
});
