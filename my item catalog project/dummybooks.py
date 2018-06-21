from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, BookDB, User

engine = create_engine('sqlite:///BookCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="rohini.chodisetty@gmail.com")
session.add(User1)
session.commit()

# Dummy books data
book1 = BookDB(bookName="Digital Fortress",
               authorName="DanBrown",
               coverUrl="""https://in.pinterest.com/
               pin/481392647662076199/""",
               description="a techno thriller",
               category="thriller", user_id=1)

session.add(book1)
session.commit()

book2 = BookDB(bookName="SorceresRing",
               authorName="Morgan Rice",
               coverUrl="""https://in.pinterest.com/
               pin/418553359095569952/""",
               description="a royal fantasy series",
               category="Fantasy", user_id=1)

session.add(book2)
session.commit()

book3 = BookDB(bookName="Harappa The curse of blood river",
               authorName="Vineeth bajpai",
               coverUrl="""https://in.pinterest.com/
               pin/375135843952518897/""",
               description="a stunning mythological series",
               category="Fantasy", user_id=1)

session.add(book3)
session.commit()

book4 = BookDB(bookName="The Ramachandra Series",
               authorName="Amish Tripathi",
               coverUrl="""https://in.pinterest.com/pin/
               719309371707011842/""",
               description="Mind blowing Historical series",
               category="Mythologoical", user_id=1)

session.add(book4)
session.commit()

book5 = BookDB(bookName="Two States",
               authorName="Chetan Bhagath",
               coverUrl="""https://in.pinterest.com/
               pin/568931365399333604/""",
               description="A indian love story",
               category="Romance", user_id=1)

session.add(book5)
session.commit()


print ("added Books!")
