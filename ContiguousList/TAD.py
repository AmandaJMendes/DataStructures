class Product:
    def __init__(self, p_id, p_name, p_price):
        """
        Constructor
        """
        self._ID = p_id
        self._name = p_name
        self._price = p_price
        
    @property
    def ID(self):
        """
        ID getter
        """
        return self._ID
    
    @property
    def name(self):
        """
        Name getter
        """
        return self._name
    
    @property
    def price(self):
        """
        Price getter
        """
        return self._price
    
    @name.setter
    def name(self, new_name):
        """
        Name setter
        """
        self._name = new_name
        
    @price.setter
    def price(self, new_price):
        """
        Price setter
        """
        self._price = new_price
        
    def __str__(self):
        """
        Representation of product as string.
        This special method is called by the print statement
        """
        return f"-- Product: {self._name}\n-- ID: {self._ID}\n-- Price: {self._price}"
    
    def __repr__(self):
        """
        Representation of product as string
        """
        return f"Prodcut object (ID {self.ID})"
    