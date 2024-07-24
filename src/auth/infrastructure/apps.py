from importlib import import_module

from django.apps import AppConfig
from django.utils.module_loading import module_has_submodule


class AuthConfig(AppConfig):
    name = "src.auth.infrastructure"
    label = "pingguardian_auth"

    def import_models(self):
        # Dictionary of models for this app, primarily maintained in the
        # 'all_models' attribute of the Apps this AppConfig is attached to.
        self.models = self.apps.all_models[self.label]

        if module_has_submodule(self.module, "persistence.database.models"):
            models_module_name = "%s.%s" % (self.name, "persistence.database.models")
            self.models_module = import_module(models_module_name)
