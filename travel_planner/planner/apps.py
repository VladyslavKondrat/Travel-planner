from django.apps import AppConfig


class PlannerConfig(AppConfig):
    name = "planner"


    def signal(self):
        import planner.signals
