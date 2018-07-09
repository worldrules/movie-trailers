# fresh tomatoes is the module necessary for generating the final html document
import fresh_tomatoes

# media is where the Movie class is defined
import media

fight_club = media.Movie("Fight Club",
                         "1999",
                         "An insomniac office worker crosses"
                         " paths with a devil-may-care soapmaker, "
                         "forming an underground fight club"
                         " that evolves into something much, much more.",
                         "http://bit.ly/2u5dCyX",
                         "https://youtu.be/SUXWAEX2jlg")

magnolia = media.Movie("Magnolia",
                       "1999",
                       "An epic mosaic of interrelated characters in"
                       " search of love, forgiveness, and "
                       "meaning in the San Fernando Valley.",
                       "http://bit.ly/2z8othi",
                       "https://youtu.be/cxcegktcxSM")

high_fidelity = media.Movie("High Fidelity",
                            "2000",
                            "Rob, a record store owner and compulsive list"
                            " maker, recounts his top five"
                            " breakups, including the one in progress.",
                            "http://bit.ly/2tXmszw",
                            "https://youtu.be/6P4dXJ_Tvns")

vanilla_sky = media.Movie("Vanilla Sky",
                          "2001",
                          "A self-indulgent and vain publishing"
                          " magnate finds his privileged life upended after"
                          " a vehicular accident with a resentful lover.",
                          "http://bit.ly/2KRIB8P",
                          "https://youtu.be/k09OX40NLUw")

the_nice_guys = media.Movie("The Nice Guys",
                            "2016",
                            "In 1970s Los Angeles, a mismatched pair "
                            "of private eyes investigate a missing "
                            "girl and the mysterious death of a porn star.",
                            "http://bit.ly/2KNyGBf",
                            "https://youtu.be/GQR5zsLHbYw")

three_billboards = media.Movie("Three Billboards Outside Ebbing, Missouri",
                               "2017",
                               "A mother personally challenges the"
                               " local authorities to solve her daughter's "
                               "murder when they fail to catch the culprit.",
                               "http://bit.ly/2IUkx3u",
                               "https://youtu.be/Jit3YhGx5pU")

# lists all the movies in order so the fresh_tomatoes function works properly
movies = [fight_club, magnolia, high_fidelity,
          vanilla_sky, the_nice_guys, three_billboards]

# fresh tomatoes function call
fresh_tomatoes.open_movies_page(movies)
