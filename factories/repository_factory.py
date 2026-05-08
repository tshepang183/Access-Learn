from repositories.inmemory.inmemory_course_repository import InMemoryCourseRepository

class RepositoryFactory:

    @staticmethod
    def get_course_repository(storage_type):

        if storage_type == "MEMORY":
            return InMemoryCourseRepository()

        elif storage_type == "DATABASE":
            # Future implementation
            return None

        else:
            raise ValueError("Invalid storage type")