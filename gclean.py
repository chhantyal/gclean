import getpass
import datetime
import gmail

# If an email is not read for following days,
# it is considered unwanted email
OLD_DAYS = 15

# To automate with crontab, add username and password
# Otherwise, interactive command prompt is used
USERNAME = None
PASSWORD = None

# By default, old unread messages are archived
# If set False, they will be deleted
# It is recommended to archive, instead of delete
ARCHIVE = True

def get_old_unread_messages(instance):
    """
    Returns list of emails which are older than days given in above setting.
    """
    today = datetime.datetime.today()
    date_filter = today - datetime.timedelta(days=OLD_DAYS)
    old_unread_messages = instance.inbox().mail(unread=True, before=date_filter)
    return old_unread_messages

def clean_gmail(username, password):
    """
    Archive or delete (default archive) old unread messages.
    """
    g = gmail.login(username, password)
    old_unread_messages = get_old_unread_messages(g)
    print '%s unread old messages in your inbox!' % len(old_unread_messages)
    print 'Cleaning in progress!'
    for message in old_unread_messages:
        if ARCHIVE:
            print 'Message %s is being archived!' % message.uid
            message.archive()
        else:
            print 'Message %s is being deleted!' % message.uid
            message.delete()
    print 'All cleaning done!'

if __name__ == "__main__":
    if USERNAME and PASSWORD:
        clean_gmail(USERNAME, PASSWORD)
    else:
        username = raw_input('GMail username: ')
        password = getpass.getpass('Password: ')
        clean_gmail(username, password)
