import { IAccountCardProps } from './account-card.types';

function AccountCard({ name, number, currency, balance }: IAccountCardProps) {
  return (
    <div className="my-1 px-1 w-full md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3">
      <article className="overflow-hidden rounded-lg shadow-lg">
        <h2 className="text-black text-center dark:text-white  text-3xl font-bold">
          {currency} {balance}
        </h2>
        <div className="flex items-center justify-between leading-tight p-2 md:p-4">
          <h3 className="text-lg">
            <span className="text-xs inline-block py-1 px-2.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-red-600 text-white rounded-full">
              Nombre:
            </span>{' '}
            {name}
          </h3>
          <p className="text-grey-darker text-sm">
            <span className="text-xs inline-block py-1 px-2.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-red-600 text-white rounded-full">
              Cuenta:
            </span>{' '}
            {number}
          </p>
        </div>
      </article>
    </div>
  );
}

export { AccountCard, AccountCard as default };
