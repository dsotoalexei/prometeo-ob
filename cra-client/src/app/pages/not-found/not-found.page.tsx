import { Link } from 'react-router-dom';

function NotFoundPage() {
  return (
    <div
      className="
    flex
    items-center
    justify-center
    h-screen
    bg-gradient-to-r
    from-indigo-600
    to-blue-400
  "
    >
      <div className="px-40 py-20 bg-white rounded-md shadow-xl">
        <div className="flex flex-col items-center">
          <h1 className="font-bold text-blue-600 text-9xl">404</h1>

          <h6 className="mb-2 text-2xl font-bold text-center text-gray-800 md:text-3xl">
            <span className="text-red-500">Oops!</span> Página no encontrada
          </h6>

          <p className="mb-8 text-center text-gray-500 md:text-lg">
            La página que buscas no existe.
          </p>

          <Link
            to="/"
            className="px-6 py-2 text-sm font-semibold text-blue-800 bg-blue-100"
          >
            Ir al Tablero
          </Link>
        </div>
      </div>
    </div>
  );
}

export { NotFoundPage, NotFoundPage as default };
