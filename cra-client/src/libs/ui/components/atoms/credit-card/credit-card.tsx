import { ICreditCardProps } from './credit-card.types';

function CreditCard({
  name,
  number,
  close_date,
  due_date,
  balance_dollar,
  balance_local,
}: ICreditCardProps) {
  return (
    <div className="rounded-2xl overflow-hidden shadow-lg">
      <div className="flex justify-center p-10 bg-gradient-to-r from-red-300 via-blue-500 to-red-300">
        <div className="w-64 h-40 bg-gradient-to-r from-blue-700 via-blue-800 to-gray-900 rounded-lg shadow-lg">
          <div className="flex justify-between m-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="34"
              height="34"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="#ffffff"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none" />
              <rect x="3" y="5" width="18" height="14" rx="3" />
              <line x1="3" y1="10" x2="21" y2="10" />
              <line x1="7" y1="15" x2="7.01" y2="15" />
              <line x1="11" y1="15" x2="13" y2="15" />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="34"
              height="34"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="#ffffff"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none" />
              <circle cx="9.5" cy="9.5" r="5.5" fill="#fff" />
              <circle cx="14.5" cy="14.5" r="5.5" />
            </svg>
          </div>
          <div className="flex justify-center mt-4">
            <h1 className="text-gray-400 font-thin font-os">{number}</h1>
          </div>
          <div className="flex flex-col justfiy-end mt-4 p-4 text-gray-400 font-quick">
            <h4 className="uppercase tracking-wider font-semibold text-xs">
              {name}
            </h4>
          </div>
        </div>
      </div>
      <div className="container mx-auto px-20">
        <div className="flex flex-col w-full">
          <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 my-2 w-full">
            <div className="metric-card bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-lg p-4 max-w-72 w-full">
              <div className="flex items-center text-gray-900 dark:text-gray-100">
                <span className="text-xs inline-block py-1 px-2.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-blue-600 text-white rounded-full">
                  Balance UYU
                </span>
              </div>
              <p className="mt-2 text-3xl font-bold spacing-sm text-black dark:text-white">
                {balance_local}
              </p>
            </div>
            <div className="metric-card bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-lg p-4 max-w-72 w-full">
              <div className="flex items-center text-gray-900 dark:text-gray-100">
                <span className="text-xs inline-block py-1 px-2.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-blue-600 text-white rounded-full">
                  Balance USD
                </span>
              </div>
              <p className="mt-2 text-3xl font-bold spacing-sm text-black dark:text-white">
                {balance_dollar}
              </p>
            </div>
          </div>
          <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 my-2 w-full">
            <div className="metric-card bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-lg p-4 max-w-72 w-full">
              <div className="flex items-center text-gray-900 dark:text-gray-100">
                <span className="text-xs inline-block py-1 px-2.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-red-600 text-white rounded-full">
                  Fecha de cierre
                </span>
              </div>
              <p className="mt-2 text-3xl font-bold spacing-sm text-black dark:text-white">
                {close_date}
              </p>
            </div>
            <div className="metric-card bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-lg p-4 max-w-72 w-full">
              <div className="flex items-center text-gray-900 dark:text-gray-100">
                <span className="text-xs inline-block py-1 px-2.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-red-600 text-white rounded-full">
                  Fecha de vencimiento
                </span>
              </div>
              <p className="mt-2 text-3xl font-bold spacing-sm text-black dark:text-white">
                {due_date}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export { CreditCard, CreditCard as default };
