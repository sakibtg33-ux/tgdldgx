# plugins/settings/settings.py
# এটি একটি ডামি ফাইল – যাতে সব ইম্পোর্ট ঠিক হয়

class OpenSettings:
    """ডামি ক্লাস – যাতে callbacks.py-তে OpenSettings ইম্পোর্ট করলে কাজ করে"""
    @staticmethod
    def get_settings():
        return {
            "caption": None,
            "thumbnail": None,
            "upload_as_doc": False
        }

# যদি আরও কোনো ফাংশন বা ভেরিয়েবল ইম্পোর্ট করা হয়, সেগুলো এখানে যোগ করুন
# যেমন:
# def some_function():
#     return True

# ইম্পোর্ট করার জন্য কিছু ডামি ভেরিয়েবল
DEF_CAPTION = None
DEF_THUMB = None
UPLOAD_AS_DOC = False
