import { useEffect } from 'react';
import { IAccountModel } from '../../../libs/domains/models';
import {
  accountsSelector,
  fetchAccounts,
  useAppDispatch,
  useAppSelector,
} from '../../../libs/redux';
import { AccountCard, EmptyRow, Loader } from '../../../libs/ui/components';

function AccountsPage() {
  const dispatch = useAppDispatch();
  const { accounts, isFetching, isError } = useAppSelector(accountsSelector);

  useEffect(() => {
    dispatch(fetchAccounts());
  }, [dispatch]);

  if (isFetching) {
    return <Loader />;
  }

  if (isError) {
    return <EmptyRow />;
  }

  return (
    <div className="container my-12 mx-auto px-4 md:px-12">
      <div className="flex flex-wrap -mx-1 lg:-mx-4">
        {accounts.map((account: IAccountModel) => (
          <AccountCard key={account?.id} />
        ))}
      </div>
    </div>
  );
}

export { AccountsPage, AccountsPage as default };
