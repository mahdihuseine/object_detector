from setuptools import setup, find_packages

setup(
    name="object_detector",  # نام جدید کتابخانه شما
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'ultralytics',
        'numpy',
    ],
    entry_points={  # اگر تابع main وجود داشته باشد، این قسمت را به‌روز کنید
        'console_scripts': [
            'object-detector=object_detector.detect:main',  # نام تابع main که در آن کارهای اصلی انجام می‌شود
        ],
    },
    include_package_data=True,
    description="A library for car and license plate detection",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/mahdihuseine/object_detector",  # آدرس گیت‌هاب یا صفحه پروژه شما
    author="Mahdihuseine",  # نام شما
    author_email="Mahdihuseine001@gmail.com",  # ایمیل شما
    license="MIT",
)
