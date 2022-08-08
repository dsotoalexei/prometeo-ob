import { useEffect } from 'react';
import { ICardModel } from '../../../libs/domains/models';
import {
  cardsSelector,
  fetchCards,
  useAppDispatch,
  useAppSelector,
} from '../../../libs/redux';
import { CreditCard, EmptyRow, Loader } from '../../../libs/ui/components';

function CreditCardsPages() {
  const dispatch = useAppDispatch();
  const { cards, isFetching, isError } = useAppSelector(cardsSelector);

  useEffect(() => {
    dispatch(fetchCards());
  }, [dispatch]);

  if (isFetching) {
    return <Loader />;
  }

  if (isError) {
    return <EmptyRow />;
  }

  return (
    <div className="p-8">
      {cards.map((card: ICardModel) => (
        <CreditCard
          key={card?.id}
          name={card?.name}
          number={card?.number}
          balance_dollar={card?.balance_dollar}
          balance_local={card?.balance_local}
          close_date={card?.close_date}
          due_date={card?.due_date}
        />
      ))}
    </div>
  );
}

export { CreditCardsPages, CreditCardsPages as default };
