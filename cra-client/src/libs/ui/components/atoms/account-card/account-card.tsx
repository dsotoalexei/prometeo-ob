import { IAccountCardProps } from './account-card.types';

function AccountCard({ name, number, currency, balance }: IAccountCardProps) {
  return (
    <div className="my-1 px-1 w-full md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3">
      <article className="overflow-hidden rounded-lg shadow-lg">
        <h2 className="text-black text-center dark:text-white  text-3xl font-bold">
          {currency} {balance}
        </h2>
        <div className="flex items-center justify-between leading-tight p-2 md:p-4">
          <h1 className="text-lg">{name}</h1>
          <p className="text-grey-darker text-sm">{number}</p>
        </div>

        <div className="flex items-center justify-between leading-none p-2 md:p-4">
          <img
            alt="Account information"
            className="block rounded-full h-20 w-20"
            src="assets/images/account.svg"
          />
          <p className="ml-2 text-sm">{currency}</p>
        </div>
        <div className="p-8 flex justify-center">
          <button className="inset-y-1 p-3 rounded-full bg-gradient-to-r from-red-600 via-red-400 to-red-600 text-white font-semibold">
            Ver movimientos
          </button>
        </div>
      </article>
    </div>
  );
}

export { AccountCard, AccountCard as default };
