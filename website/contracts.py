class ErrorCodes:
    USER_NOT_LOGGED_IN = 1
    OBJECT_NOT_SAVED = 2


class SessionParameters:
    USERID = "userid"


class RecommendationContractRequest:
    # RECOMMENDATION PAYLOAD FIELDS
    OCCASION_KEY = "occasion"
    CITY_KEY = "city"
    DATE_TIME_KEY = "dateTime"
    TIME_KEY = "time"
    AGE_GROUP_KEY = "ageGroup"
    CULTURE_KEY = "culture"
    GENDER_KEY = "gender"

class NewRecommendationContractRequest:
    # RECOMMENDATION PAYLOAD FIELDS
    GENDER_KEY = "gender"
    MASTER_CATEGORY_KEY = "masterCategory"
    SUB_CATEGORY_KEY = "subCategory"
    ARTICLE_TYPE_KEY = "articleType"
    BASE_COLOUR_KEY = "baseColour"
    SEASON_KEY = "season"
    USAGE_KEY = "usage"


class RecommendationContractResponse:
    LINKS = "links"

class NewRecommendationContractResponse:
    IMAGES = "images"


class PreferenceContractRequest:
    PREFERENCES = "preferences"


class FavouritesContrastRequest:
    FAVOURITE_URL_KEY = "favouriteUrl"
    SEARCH_OCCASION_KEY = "occasion"
    SEARCH_WEATHER_KEY = "city"
