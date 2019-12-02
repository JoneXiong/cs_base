import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from .hook import OdooHook
sys.meta_path.append(OdooHook())

from . import models
from . import controllers
