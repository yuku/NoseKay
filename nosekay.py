# -*- coding: utf-8 -*-
import os
import logging
import sys
from nose.plugins.base import Plugin

log = logging.getLogger(__name__)

class NoseKay(Plugin):
    name = "kay"

    def options(self, parser, env=os.environ):
        super(NoseKay, self).options(parser, env)
        parser.add_option(
            "--kay-app-dir", default=None, action="store", dest="kay_app",
            help="Set the path to the Kay application under test. Default is "
                 "current directory.")

    def configure(self, options, config):
        super(NoseKay, self).configure(options, config)
        if not self.enabled:
            return
        self.config = config
        if options.kay_app is not None:
            self._path = options.kay_app
        else:
            self._path = config.workingDir

        sys.path.append(self._path)

        try:
            import kay
        except ImportError:
            self.enabled = False
            raise ImportError("Kay application not found. You can use "
                              "--kay-app-dir option to specify your "
                              "application directory.")

        kay.setup_env()

        import kay.management

        kay.management.test.setup_env()
        kay.management.test.setup_stub()

        if sys.version_info[0:2] < (2,5):
            raise EnvironmentError(
                "Python version must be 2.5 or greater, like the Google App "
                "Engine environment. Tests are running with: %s" % sys.version)

        # remove StreamHandler
        rootLogger = logging.getLogger()
        for handler in rootLogger.handlers:
            if isinstance(handler, logging.StreamHandler):
                rootLogger.removeHandler(handler)
