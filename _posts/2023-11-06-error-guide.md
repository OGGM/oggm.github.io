---
layout: post
title: "Help, an error!"
subtitle: "A short guide on what to do when you get stuck or have a question"
author: Anouk Vlug and Jenna Sutherland
date: 2023-11-02T00:00:00
tags: community programming model
---

When you start using OGGM, it is very likely that you will have many questions, and at some point, you will inevitably encounter an error while running your script. We have noticed that those who are new to OGGM, and to coding in general, sometimes struggle to handle these situations efficiently. Some may wrestle with the issue on their own for too long, while others bombard the community with an overload of questions, which can become exhausting. And there are those who might panic at the sight of an error.

*Please don’t panic!* We're here to guide you step-by-step through what to do when you encounter an error or have a question.

## Try to find the solution by yourself

The first step is to try to resolve the issue on your own. You can, for instance:

- Read the [documentation](https://docs.oggm.org/en/stable/) and go through the [tutorials](https://oggm.org/tutorials/stable/notebooks/welcome.html).
- Check the [docstring](https://www.geeksforgeeks.org/python-docstrings/) of the function you are attempting to use, or search for the function description in the [list of OGGM functions and tasks](https://docs.oggm.org/en/stable/api.html).
- Delve deeper into the code you're utilizing by [browsing the code on GitHub](https://github.com/OGGM/oggm).
- Try some [debugging](https://code.visualstudio.com/docs/editor/debugging).
- In some cases, it might also be useful to review the [recent publication list](https://oggm.org/publications/), explore [OGGM-edu](https://edu.oggm.org/en/latest/), or the [blog posts](https://oggm.org/search/index.html).

**The debugger is probably the tool most overlooked by scientists when writing code with OGGM**. Unlike commonly used libraries such as Numpy or Xarray, OGGM may require users to understand the behind-the-scenes workings. A debugger—an excellent tool for pausing code execution at any point to explore the state of the variables at that particular moment—is invaluable for grasping what a model or function is doing.

## Asking a question

If, after a serious attempt, you haven't succeeded in finding the answer yourself, it might be time to ask a question. Fortunately, OGGM has an active community ready to assist. Since community members respond to questions on a voluntary basis, please be considerate, avoid overwhelming them, and pose your questions clearly and concisely. This advice is particularly pertinent if you're relatively new to programming. The following sections will guide you through where and how to ask your question, how to manage your expectations, and how to close the question or issue once it has been resolved.

### Where to ask your question

Typically, no OGGM coding support is provided via email. Most questions are best asked in the `#support` channel on the OGGM [Slack](https://oggm.org/2022/10/11/Welcome-to-the-OGGM-Slack/), our internal communications platform, where you will likely receive the quickest response. However, if you have numerous questions or prefer a more interactive discussion about the issue, feel free to join our online [community meetings](https://oggm.org/meetings/). If you are working on code development or encounter a bug in the codebase, raising an [issue on GitHub](https://github.com/OGGM/oggm/issues) in one of the OGGM repositories may be more appropriate.

### How to ask your question

Before you ask your question, do a quick check to see if it has already been addressed. Crafting a clear, detailed question may require some effort, but it's crucial for obtaining a helpful response. Avoid vague queries like "I got error XXX, how do I solve this?" without providing any context. Instead, provide as much detail as possible to give your question context. Below is a structured approach to formulating your question, complete with everyday analogies to illustrate the importance of each element:

- **What you are trying to achieve:**
  - e.g., I’m attempting to project global glacier changes for the coming century (akin to wanting to enter the seminar room).
- **Why you want to achieve it:**
  - e.g., To assess the impact of feature X after integrating my module (comparable to checking if I can connect my laptop for a presentation next week).
- **How you are trying to achieve it:**
  - e.g., The Python code I’m using (like going to the seminar room).
  - _When sharing code, please share it as a script not a print screen._
- **Why it is not working:**
  - e.g., The full error log (as if the seminar room is locked, and I don’t have a key).
- **What you have already tried:**
  - e.g., I have followed several tutorials without finding an answer (like asking the secretary and the concierge for a key, to no avail).
- **Pose your question:**
  - e.g., Does anyone know how to solve this error? (Can someone help me get into the seminar room?)

Skipping steps may lead to misunderstandings or non-useful responses. It's possible that solutions you've already tried or ones that don't meet your requirements will be suggested. Furthermore, by not sharing all relevant information, you might miss out on potential solutions. For the specific example above, it might be useful to know that OGGM provides [standard projections](https://docs.oggm.org/en/stable/download-projections.html) (or that a colleague is aware of all available adapters in the seminar room). Thus, omitting essential details can waste both your and your colleagues' time.

### The reply

After posing your question, the next step is to wait patiently for a reply. Community members volunteer their time to answer questions and come from different work cultures with varying hours, so don't expect immediate responses over the weekend, for instance. If your issue is resolved in the meantime, please inform the community.

On Slack, adding additional information to the question and follow-up discussions should occur in the thread related to your question to maintain organization. On GitHub, conversations continue within the respective issue. In either case, make it clear when a solution has been found. On GitHub, you can close the issue; on Slack, mark the main question with a ✅ emoji to indicate it has been answered. It's a kind gesture to thank those who helped you, and remember to offer help to others when you can.

