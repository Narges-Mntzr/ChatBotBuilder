## چت‌بات‌ساز (Chatbot Maker)

در این پروژه قصد داریم یک سایت توسعه دهیم که در آن تعدادی از کاربران بتوانند برای دیتای مورد نظر خودشون chatBot بسازن. به این ترتیب که ابتدا دیتای مورد نظرشون رو در نرم‌افزار وارد میکنن (knowledge base) و بعد بتونن چت باتی بسازن که با توجه به دیتای وارد شده در مرحله قبل به سوالات کاربرها جواب بده.
و همچنین بقیه کاربران می‌توانند گفت و گوهایی با این بات‌های ساخته شده ایجاد کنند و با توجه به محتوای آن‌ها از آن‌ها سوال بپرسند.

## تکنولوژی‌های استفاده شده در پروژه:

1.قسمت اصلی و بدنه پروژه با فریمورک django پیاده‌سازی شده است.<br />
2.پایگاه‌داده مورد استفاده در پروژه postgres می‌باشد. (برای استفاده از اکتنشن pgvector از ایمیج ankane/pgvector استفاده شده است)<br /><br />

## کاربران پروژه:

### Torob Admin

ادمین سایت که دسترسی به اطلاعات تمامی کاربران، بات‌ها، محتواها و گفتگوهای ساخته شده را دارد و می‌تواند آن‌ها را اضافه، حذف و یا ویرایش کند.

### Chatbot Maker

گروهی از کاربران که ادمین سایت به آنها دسترسی ساخت بات‌های جدیدی را داده است. این گروه از کاربران می‌توانند بات‌ها و محتواهایی که توسط آن‌ها ایجاد شده است را ببینند و در صورت نیاز آن‌ها را ویرایش کنند.

### Normal User

این دسته تمامی کاربران سایت را شامل می‌شود که می‌توانند در سایت ثبت‌نام کنند و پس از ورود به سایت با بات‌هایی که در سایت موجود است گفت و گوی جدیدی را آغاز کنند.

همچنین می‌توانند گفتگو‌های قبلی خود را دیده و در صورت فعال بودن بات گفتگو را ادامه دهند.

## فرآیندهای اصلی سایت:

### ساخت چت‌بات جدید
تفاوت اصلی این سایت با سایت‌هایی مانند chatGPT در این مرحله است. گروهی از کاربران می‌توانند برای کسب و کار خود یک چت‌بات ایجاد کنند و محتواهای مرتبط با کار خود را در آن قرار دهند. سپس تمام آن محتوا‌ها به یک آرایه نظیر می‌شود و در هر مرحله پاسخ کاربر با توجه به شبیه‌ترین محتوا به آن داده می‌شود.

### صفحه اصلی + Full text search
اولین صفحه‌ای که کاربر در شروع می‌بیند لیستی از گفت‌و‌گوهایی است که در گذشته داشته است. در این مرحله کاربر می‌تواند روی گفت‌و‌گوهای خود باتوجه به عنوان و متن پیام‌های گفتگو جستجو انجام دهد. در این جستجو نه تنها همان عبارت بلکه تمام کلمات هم ریشه آن‌هم در نظر گرفته می‌شود.

### شروع گفت‌وگو
کاربر هر زمان که بخواهد می‌تواند گفت‌وگوهای قبلی خود را ادامه و یا با هر یک از بات‌های فعال گفت‌و‌گوی جدیدی را شروع کند. پس از شروع گفت‌و‌گو با هر پیامی که از طرف کاربر برای بات فرستاده می‌شود ابتدا محتوای سوال کاربر به یک آرایه نظیر می‌شود. و سپس شبیه‌ترین محتوای بات براساس الگوریتم مورد نظر تشخیص داده شده و طبق ساختار زیر در prompt پیام قرار می‌گیرد.

    "{self.related_botcontent.text}"
    Based on the above document and your own information, give a step-by-step and acceptable answer to the following question.
    Question: {self.text}

### ارسال سوال و دریافت پاسخ
پس از تهیه پرامپت سوال، طبق ساختار زیر سوال برای gpt ارسال و پس از دریافت پاسخ به کاربر نشان داده می‌شود.

    messages: system prompt + prompt of preQuestion + answer of preQuestion + prompt of this question
* سیستم پرامپت در زمان ساخت بات توسط سازنده تعیین شده است و همیشه ابتدای پیام‌ها آورده می‌شود. در سیستم پرامپت مشخص مواردی که چت‌بات باید در پاسخ‌های خود در نظر بگیرد گفته می‌شود.


## OpenAI
ارتباط با OpenAI به صورت جزئی‌تر در زیر توضیح داده شده است.
### embedding
محتواهای ذخیره شده برای بات و پیام‌ها بعد از ایجاد به کمک مدل "text-embedding-ada-002" به یک آرایه با 1536 درایه و نرم ۱ نظیر می‌شوند. سپس این آرایه به کمک اکستنشن pgvector ذخیره می‌شود.

### similarity
شباهت سوالات کاربر و محتواها به کمک تابع CosineDistance بررسی و شبیه‌ترین محتوا در کنار سوال قرار می‌گیرد.

<p align="center">
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/15d11df2d48da4787ee86a4b8c14551fbf0bc96a" width="800" height="100" alt="accessibility text">
</p>



### prompts
بعد از پیدا کردن شبیه‌ترین محتوا ریکوستی به مدل gpt-3.5-turbo زده‌می‌شود که شامل سیستم پرامپت ذخیره شده در بات، سوال قبلی کاربر، محتوای نظیر آن، پاسخ مدل، سوال کنونی کاربر و محتوای مرتبط با آن است.

سوالات و محتواهای مرتبط با آن‌ها با قالب زیر برای مدل فرستاده می‌شود.

    
### test similarity
 عملکرد تابع شباهت به کمک یک دیتاست با ۵۸۴ محتوا و سوال اندازه‌گیری می‌شود. به این صورت که یک کلاس تست نوشته شده است که ۱۰۰ عدد از محتواها را به صورت تصادفی انتخاب می‌کند و آن‌ها را به باتی اضافه می‌کند سپس شروع به پرسیدن این ۱۰۰ سوال می‌کند و به ازای هر سوال که محتوای خروجی تابع similar_content و محتوا درون دیتاست یکسان بود مقدار trueAnswers را یکی افزایش می‌دهد.

 بعد از اتمام صد سوال مقدار trueAnswers را در فایل django.log لاگ می‌اندازد.که عملکرد این تابع در سه بار اجرای تابع تست به صورت زیر می‌باشد.

 | trueAnswers | 97/100 | 97/100 | 99/100 |
 | ----------- | ------ | ------ | ------ |

و عملکرد تابع یکبار روی کل دیتاست بررسی شد که خروجی به صورت زیر بود.

 | trueAnswers | 557/584 |
 | ----------- | ------- |


## مدل‌های مورد استفاده

### 1. User

مدل user پیش‌فرض خود django که برای کاربران مقدار email برای username در نظرگرفته شده است.
و هم چنین هر کاربر یک username، password و group دارد.

### 2. Bot:
بات‌ها فقط توسط ادمین و کاربرانی که توسط ادمین در گروه chatbot Maker قرار گرفته‌اند ساخته می‌شود.

    user: ForeignKey(User) #کاربری که بات را ساخته
    title: CharField(20)
    detail: TextField(1000)
    img: ImageField # در ولمی که برای کانتیرها ساخته شده ذخیره می‌شود
    prompt: TextField(1000) #سیستم پرامپت‌های درخواست‌های مرتبط با این بات
    is_active: BooleanField

### 3. BotContent
هر بات می‌تواند بسته به عملکرد مورد نظر خود چندین محتوا داشته باشد که توسط سازنده بات در آن قرار داده شده است. البته هر محتوا می‌تواند حداکثر ۸۰۰ کاراکتر باشد.

    bot: ForeignKey(Bot)
    text: TextField(800)
    embedding = VectorField(dimensions=1536) #به صورت اتوماتیک با توجه به متن پیام محاسبه می‌شود.

### 4. Chat

    user: ForeignKey(User) #کاربری که گفت‌و‌گو را ساخته
    bot: ForeignKey(Bot)
    title: CharField(30) #به صورت خودکار بعد از اولین پیام ایجاد می‌شود.
    preview: TextField(50) #مرتبط با اولین پیام
    create_date: DateTimeField
    last_message_date: models.DateTimeField #به صورت خودکار به کمک سیگنال‌ها بعد از هر پیام به‌روز می‌شود.

### 5. Message

    class Reaction: TextChoices(LIKE, DISLIKE, NONE)
    class Role: TextChoices(BOT, USER)

    chat: ForeignKey(Chat)
    previous_message: ForeignKey(Message)
    text: TextField(800)
    pub_date: DateTimeField
    role: CharField(choices=Role.choices)
    reaction: CharField(choices=Reaction.choices)
    related_botcontent: ForeignKey(BotContent) #به‌دست آمد به کمک تابع امبدینگ و بررسی میزان شباهت

    def get_prompt(self):
        f'''
        "{self.related_botcontent.text}"
        Based on the above document and your own information, give a step-by-step and acceptable answer to the following question.
        Question: {self.text}
        '''

 ## اجرای برنامه
 1. docker build -t DOCKER_IMAGE .
 2. set DOCKER_IMAGE and OPENAI_API_KEY in docker compose
 3. docker compose up -d

see: https://chatbotmaker.darkube.app/