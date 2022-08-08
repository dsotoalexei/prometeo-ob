import { useState } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { Transition } from '@headlessui/react';
import { fetchLogout, useAppDispatch } from '../../../../redux';

function NavBar() {
  const dispatch = useAppDispatch();
  const [isOpen, setIsOpen] = useState<boolean>(false);

  const onLogOut = () => {
    localStorage.removeItem('accessKey');
    dispatch(fetchLogout());
  };

  return (
    <div>
      <nav className="bg-red-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <Link to="/">
                  <img
                    className="h-8 w-250"
                    src="assets/images/logo/logo.png"
                    alt="Prometeo"
                  />
                </Link>
              </div>
              <div className="hidden md:block">
                <div className="ml-10 flex items-baseline space-x-4">
                  <NavLink
                    to="/"
                    className={({ isActive }) =>
                      isActive
                        ? 'hover:bg-red-900 text-white px-3 py-2 rounded-md text-sm font-medium'
                        : 'text-gray-300 hover:bg-red-900 hover:text-white px-3 py-2 rounded-md text-sm font-medium'
                    }
                  >
                    Tablero
                  </NavLink>

                  <NavLink
                    to="/accounts"
                    className={({ isActive }) =>
                      isActive
                        ? 'hover:bg-red-900 text-white px-3 py-2 rounded-md text-sm font-medium'
                        : 'text-gray-300 hover:bg-red-900 hover:text-white px-3 py-2 rounded-md text-sm font-medium'
                    }
                  >
                    Cuentas
                  </NavLink>

                  <NavLink
                    to="/credit-cards"
                    className={({ isActive }) =>
                      isActive
                        ? 'hover:bg-red-900 text-white px-3 py-2 rounded-md text-sm font-medium'
                        : 'text-gray-300 hover:bg-red-900 hover:text-white px-3 py-2 rounded-md text-sm font-medium'
                    }
                  >
                    Tarjetas de crédito
                  </NavLink>
                  <button
                    type="button"
                    onClick={onLogOut}
                    className="text-gray-300 hover:bg-red-900 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                  >
                    Cerrar sesion
                  </button>
                </div>
              </div>
            </div>
            <div className="-mr-2 flex md:hidden">
              <button
                onClick={() => setIsOpen(!isOpen)}
                type="button"
                className="bg-gray-900 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white"
                aria-controls="mobile-menu"
                aria-expanded="false"
              >
                <span className="sr-only">Open main menu</span>
                {!isOpen ? (
                  <svg
                    className="block h-6 w-6"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M4 6h16M4 12h16M4 18h16"
                    />
                  </svg>
                ) : (
                  <svg
                    className="block h-6 w-6"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                )}
              </button>
            </div>
          </div>
        </div>

        <Transition
          show={isOpen}
          enter="transition ease-out duration-100 transform"
          enterFrom="opacity-0 scale-95"
          enterTo="opacity-100 scale-100"
          leave="transition ease-in duration-75 transform"
          leaveFrom="opacity-100 scale-100"
          leaveTo="opacity-0 scale-95"
        >
          {() => (
            <div className="md:hidden" id="mobile-menu">
              <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <NavLink
                  to="/"
                  className={({ isActive }) =>
                    isActive
                      ? 'hover:bg-red-900 text-white block px-3 py-2 rounded-md text-base font-medium'
                      : 'text-gray-300 hover:bg-red-900 hover:text-white block px-3 py-2 rounded-md text-base font-medium'
                  }
                >
                  Tablero
                </NavLink>

                <NavLink
                  to="/accounts"
                  className={({ isActive }) =>
                    isActive
                      ? 'hover:bg-red-900 text-white block px-3 py-2 rounded-md text-base font-medium'
                      : 'text-gray-300 hover:bg-red-900 hover:text-white block px-3 py-2 rounded-md text-base font-medium'
                  }
                >
                  Cuentas
                </NavLink>

                <NavLink
                  to="/credit-cards"
                  className={({ isActive }) =>
                    isActive
                      ? 'hover:bg-red-900 text-white block px-3 py-2 rounded-md text-base font-medium'
                      : 'text-gray-300 hover:bg-red-900 hover:text-white block px-3 py-2 rounded-md text-base font-medium'
                  }
                >
                  Tarjetas de crédito
                </NavLink>
                <button
                  onClick={onLogOut}
                  className="text-gray-300 hover:bg-red-900 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
                >
                  Cerrar sesion
                </button>
              </div>
            </div>
          )}
        </Transition>
      </nav>
    </div>
  );
}

export { NavBar, NavBar as default };
