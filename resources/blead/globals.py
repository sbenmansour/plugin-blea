import time
JEEDOM_COM = ''
KNOWN_DEVICES = {}
LEARN_MODE = False
LEARN_MODE_ALL = 0
LAST_VIRTUAL = int(time.time())
LAST_BEAT = int(time.time())
LEARN_BEGIN = int(time.time())
LAST_CLEAR = int(time.time())
SCAN_INTERVAL = 39
COMPATIBILITY = []
LAST_STATE={}
PRESENT={}
IGNORE=[]
KEEPED_CONNECTION={}
LAST_STORAGE={}
LAST_TIME_READ = {}
IFACE_DEVICE = 0
SCAN_ERRORS = 0
SCANNER = ''
PENDING_ACTION = False
log_level = "error"
pidfile = '/tmp/blead.pid'
apikey = ''
callback = ''
cycle = 0.3
daemonname=''
socketport=''
sockethost=''
