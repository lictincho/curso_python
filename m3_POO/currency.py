import sqlite3

DB_PATH = 'prueba.db'

class CurrencyManager(object):
    """
    Esta clase se encarga de gestionar las operaciones con una base de datos SQLite
    para almacenar información sobre diferentes monedas.
    """

    def __init__(self, database=None):
        """
        Constructor de la clase. Inicializa la conexión a la base de datos.
        """
        if not database:
            database = ":memory:"  # Si no se especifica una base de datos, se crea una en memoria
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def insert(self, obj):
        """
        Inserta un nuevo registro de moneda en la base de datos.
        """
        query = "INSERT INTO currency VALUES ('{}', '{}', '{}')".format(obj.code, obj.name, obj.symbol)
        self.cursor.execute(query)
        self.conn.commit()

class Currency(object):
    """
    Esta clase representa una moneda individual con sus atributos: código, nombre y símbolo.
    """

    objects = CurrencyManager(DB_PATH)  # Se crea un objeto CurrencyManager para interactuar con la base de datos

    def __init__(self, code, name, symbol):
        """
        Constructor de la clase. Inicializa los atributos de la moneda.
        """
        self.code = code
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        """
        Devuelve una representación en cadena de la moneda.
        """
        return u'{}'.format(self.name)

# Ejemplos de creación de objetos de tipo moneda
peso_arg = Currency(code='ARS', name='Pesos (Arg)', symbol='$')
dolar = Currency(code='USD', name='Dolar', symbol='$')
euro = Currency(code='EUR', name='Euro', symbol='€')

Currency.objects.insert(peso_arg)
Currency.objects.insert(dolar)
Currency.objects.insert(euro)