#Factory Pattern Implementation

#French Langauge Local Class
class FrenchLocalizer:
    """ it simply returns the french version """

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, message):
        """change the message using translations"""
        return self.translations.get(msg, msg)

# Spanish Language Localizer Class
class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)

# English Language Localizer
class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


#Factor Pattern Implementation
def Factory(language="English"):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

# Execution
if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print('-------------')
        print(f.localize(msg))
        print('-------------')
        print(e.localize(msg))
        print('-------------')
        print(s.localize(msg))
