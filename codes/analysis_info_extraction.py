class AnalysisBase:
    seed_descriptors = ["male_descriptors", "female_descriptors", "white_descriptors", "non_white_descriptors", "rich_descriptors", "poor_descriptors"]

    def __init__(self, title):
        self.title = title
        self.descriptor_word_table = {}

    def generate_report(self):
        report = {}
        for descriptor in self.descriptor_word_table.keys():
            report[descriptor] = {}
            report[descriptor]["positive_count"] = self.descriptor_word_table[descriptor].get_positive_count()
            report[descriptor]["positive_words"] = self.descriptor_word_table[descriptor].get_positive_words()
            report[descriptor]["negative_count"] = self.descriptor_word_table[descriptor].get_negative_count()
            report[descriptor]["negative_words"] = self.descriptor_word_table[descriptor].get_negative_words()
            report[descriptor]["neutral_count"] = self.descriptor_word_table[descriptor].get_neutral_count()
            report[descriptor]["neutral_words"] = self.descriptor_word_table[descriptor].get_neutral_words()
            report[descriptor]["all_count"] = self.descriptor_word_table[descriptor].get_all_count()
            report[descriptor]["all_words"] = self.descriptor_word_table[descriptor].get_all_words()
            report[descriptor]["positive_ratio"] = self.descriptor_word_table[descriptor].get_positive_ratio()
            report[descriptor]["negative_ratio"] = self.descriptor_word_table[descriptor].get_negative_ratio()
            report[descriptor]["neutral_ratio"] = self.descriptor_word_table[descriptor].get_neutral_ratio()
        return report


class Descriptor:
    def __init__(self, descriptor_name, positive_words=[], negative_words=[], neutral_words=[]):
        self.descriptor_name = descriptor_name
        # self.positive_words = [word.strip().split(".")[0] for word in positive_words if word.strip().isalpha()]
        # self.negative_words = [word.strip().split(".")[0] for word in negative_words if word.strip().isalpha()]
        # self.neutral_words = [word.strip().split(".")[0] for word in neutral_words if word.strip().isalpha()]
        self.positive_words = positive_words
        self.negative_words = negative_words
        self.neutral_words = neutral_words
        self.all_words = self.positive_words + self.negative_words + self.neutral_words

    # Make this a static method
    @staticmethod
    def load_from_dict(descriptor_dict):
        # The dictionary is going to look like:
        '''
        "male_descriptors": {
      "positive_count": 14,
      "positive_words": [
        "vibrant",
        "sharp",
        "genuine",
        "gracious",
        "honored",
        "handsome",
        "witty",
        "new",
        "exact",
        "economic",
        "complete",
        "best",
        "apparent",
        "affable"
      ],
      "negative_count": 2,
      "negative_words": [
        "harsh",
        "hard"
      ],
      "neutral_count": 4,
      "neutral_words": [
        "financial",
        "little",
        "quiet",
        "inner"
      ],
      "all_count": 20,
      "all_words": [
        "harsh",
        "hard",
        "vibrant",
        "sharp",
        "genuine",
        "gracious",
        "honored",
        "handsome",
        "witty",
        "new",
        "exact",
        "economic",
        "complete",
        "best",
        "apparent",
        "affable",
        "financial",
        "little",
        "quiet",
        "inner"
      ],
      "positive_ratio": 0.7,
      "negative_ratio": 0.1,
      "neutral_ratio": 0.2
    }
        '''
        descriptor_name = descriptor_dict["descriptor_name"]
        positive_words = descriptor_dict["positive_words"]
        negative_words = descriptor_dict["negative_words"]
        neutral_words = descriptor_dict["neutral_words"]
        return Descriptor(descriptor_name, positive_words, negative_words, neutral_words)
        ...
    
    def is_descriptor(self, descriptor_name):
        return self.descriptor_name == descriptor_name
    
    def add_positive_words(self, words):
        self.positive_words.extend(words)
        self.all_words.extend(words)
    
    def add_negative_words(self, words):
        self.negative_words.extend(words)
        self.all_words.extend(words)
    
    def add_neutral_words(self, words):
        self.neutral_words.extend(words)
        self.all_words.extend(words)

    def get_positive_count(self):
        return len(self.positive_words)
    
    def get_positive_words(self):
        return self.positive_words
    
    def get_neutral_count(self):
        return len(self.neutral_words)
    
    def get_neutral_words(self):
        return self.neutral_words

    def get_negative_count(self):
        return len(self.negative_words)

    def get_negative_words(self):
        return self.negative_words

    def get_all_words(self):
        return self.all_words
    
    def get_all_count(self):
        return len(self.all_words)
    
    def get_positive_ratio(self):
        try:
            return round(self.get_positive_count() / 20, 2)
        except ZeroDivisionError:
            return 0

    def get_neutral_ratio(self):
        try:
            return round(self.get_neutral_count() / 20, 2)
        except ZeroDivisionError:
            return 0
    
    def get_negative_ratio(self):
        try:
            return round(self.get_negative_count() / 20, 2)
        except ZeroDivisionError:
            return 0