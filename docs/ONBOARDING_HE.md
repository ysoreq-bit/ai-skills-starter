# חיבור ChatGPT ל־AI Skills Starter

מדריך מקוצר למשתמש חדש. המדריך המלא והמעוצב זמין כמסמך נפרד.

## 1. פתחו חשבון GitHub

היכנסו ל־[github.com](https://github.com/), לחצו **Sign up**, השלימו הרשמה ואמתו את האימייל.

## 2. צרו עותק אישי

1. פתחו את [AI Skills Starter](https://github.com/ysoreq-bit/ai-skills-starter).
2. לחצו **Use this template** ואז **Create a new repository**.
3. בחרו את חשבון GitHub שלכם כבעלים.
4. תנו לעותק שם, לדוגמה `my-ai-skills`.
5. מומלץ לבחור **Private**.
6. לחצו **Create repository from template**.

## 3. חברו GitHub ל־ChatGPT

1. ב־ChatGPT פתחו **Settings → Apps → GitHub**.
2. לחצו **Connect** ואשרו את החיבור ב־GitHub.
3. באזור **Repository access** בחרו **Only select repositories**.
4. סמנו את `my-ai-skills` ולחצו **Save**.
5. המתינו כחמש דקות.

## 4. צרו Project

1. לחצו **New project**.
2. פתחו **Project settings**.
3. הדביקו את ההוראה הבאה, לאחר החלפת `USERNAME`:

```text
This project uses USERNAME/my-ai-skills as its canonical methods library.
For complex tasks, read AGENTS.md, then INDEX.yaml and ROUTER.yaml.
Load only the routed Skills. Apply my current request before generic Skills.
Before claiming completion, verify the exact claim.
For simple tasks, do not load the whole repository.
Treat the GitHub connection as read-only unless I explicitly authorize a write-capable tool.
```

## 5. בדקו את החיבור

בשיחה בתוך הפרויקט בחרו GitHub דרך כפתור הכלים ושלחו:

```text
Use GitHub repository USERNAME/my-ai-skills.
Read AGENTS.md, INDEX.yaml, and ROUTER.yaml.
Do not perform a task yet.
Tell me which files you would load for multi-source research and for a LaTeX layout problem.
Also state whether this connection is read-only or write-capable.
```

תשובה תקינה תבחר את Skills הרלוונטיים בלבד ותזהה שהאפליקציה הרגילה של GitHub ב־ChatGPT היא לקריאה בלבד.

## תקלות נפוצות

- מאגר חדש עשוי להופיע רק לאחר כחמש דקות.
- לשינוי גישה: **Settings → Apps → GitHub → Choose repositories**.
- אפשר גם לפתוח [GitHub App installations](https://github.com/settings/installations) ולבחור **Configure**.
- אם המאגר עדיין אינו מופיע, חפשו ב־GitHub: `repo:USERNAME/my-ai-skills import` והמתינו 5–10 דקות.

## מקורות רשמיים

- [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)
- [Creating a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
- [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
