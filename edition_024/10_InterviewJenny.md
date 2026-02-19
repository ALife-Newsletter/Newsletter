# Interview with Jenny Zhang

*Jenny Zhang is an AI researcher and PhD student studying under Jeff Clune at the University of British Columbia. She took some time over the holidays to answer a few of my questions about her background, work, and the future of AI.*

— *Martha*


**M.E.** 
I became interested in open-endedness after reading Lisa Soros & Kenneth Stanley’s [chromaria paper](https://direct.mit.edu/isal/proceedings/alife2014/26/793/98965) a few years ago. You have done quite a bit of research in this area too. How did open-endedness become a focus for you?

**J.Z.**
One of the most life-changing papers I have read, and the one I credit with sparking my initial interest in open-endedness research, was [Robots that can adapt like animals](https://www.nature.com/articles/nature14422). After reading it, I reached out to Prof. Antoine Cully, a professor at the same university where I was an undergraduate, to ask about doing a research attachment with him. At the time, I did not think of this interest as "open-endedness”, I simply thought it was an incredibly cool paper with incredible results. Thankfully, Prof. Cully took me on as a student and taught me many of the skills that helped kickstart my research career.

During my undergraduate studies, I explored several other research directions, but none resonated with me as strongly as my work with Prof. Cully. As a result, when applying for a PhD, I deliberately looked for researchers he had previously collaborated with, which is how I stumbled upon Prof. Jeff Clune and his seminal work. I am deeply grateful that Prof. Clune took me on as a PhD student, and it was there that I continued to deepen my interest in open-endedness. Each year, I continue to learn so much, not only from Prof. Clune, but also from the wider research community and from everyday life experiences.

**M.E.**
I was so excited when I found [Awesome Open-Ended AI](https://github.com/jennyzzt/awesome-open-ended), your open-source collection of resources. What inspired you to create it?

**J.Z.**
I am super glad to hear that! After my first PhD project, I found myself reflecting on how much I had learned, and realized retrospectively that having a resource to help navigate the thousands of AI papers published every year would have been incredibly useful for learning more about this niche field. I also realized that even though I had read many papers, I was likely still missing a large number of works that could be deeply inspiring. Hence, I decided to create this resource and invite contributions from everyone, both to expand my own reading list and, hopefully, to provide a helpful resource for others as well.

If anyone thinks they know of a work that is relevant and not yet on the list, contributions to Awesome Open-Ended AI are always welcome!

**M.E.** 
Tell me about some of your current work.

**J.Z.**
Most recently, we released the [Darwin Gödel Machine](https://sakana.ai/dgm/) (DGM), a project done together with Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. This work was exciting from ideation to implementation, and it continues to be exciting as we envision what a scaled-up version of the DGM could eventually achieve.

Before working on the DGM, I focused on task generation to enable agents to continuously learn new and interesting tasks forever. However, across these projects, I observed that as runs become longer, agents require increasingly more iterations to learn the next new task, even when the increase in difficulty between successive tasks remains consistent. In other words, the learning rate of the agent slows down as tasks become more complex. This stands in contrast to human culture and evolution, where the rate at which new technologies are created appears to accelerate exponentially over time. I believe this gap between my earlier algorithms and human cultural evolution stems from the lack of self-referentiality and self-modification. Ideally, an algorithm should not only improve its performance over time, but also improve its ability to modify itself as it learns.

Shengran’s work on [Automated Design of Agentic Systems](https://arxiv.org/pdf/2408.08435?) demonstrated that coding agents can be used to improve performance on downstream tasks. At the same time, we noticed a growing trend of people using coding agents to automate their own coding workflows, including, in some cases, building better coding agents. This suggested that existing coding agents were already capable enough to collaborate with humans to construct improved future coding agents. Inspired by this observation, we asked: why not close the loop and allow a coding agent to autonomously improve itself over time? Closing this loop would also introduce true self-referentiality, whereby improvements in the agent’s coding ability directly translate into better future self-improvement.

Motivated by these ideas, we worked together to create a coding agent that is self-referential and self-improving in an open-ended manner, giving rise to the Darwin Gödel Machine.

Currently, I am continuing to work in a similar direction to the Darwin Gödel Machine, and hope to be able to share the full paper soon!

**M.E.**
How do you think open-endedness fits into the future of AI?

**J.Z.**
I believe that open-endedness is, and will continue to be, one of the key research directions that will allow AI to become ever more useful in society. Beyond AI research, principles from open-endedness also speak to how we navigate life, values, and long-term decisions. In many open-ended algorithms, we observe that stepping stones which may not carry the highest fitness score at first can, over time, give rise to outcomes that surpass all others. This serves as a reminder that progress does not always emerge from the most direct path, but often from a willingness to explore, to linger, and to follow curiosity into the unknown. In this co-evolution of technology and humans, I believe that open-endedness will not only play a key role in the development of AI itself, but also in the development of AI researchers, further deepening this cycle of mutual growth and co-evolution.

**M.E.**
What are your favorite things to do outside of research?

**J.Z.**
I used to do 3D printing, but stopped recently. Now, I am trying to learn how to communicate better, so I’ve been mainly reading books on communication. Wish me luck!

**M.E.**
Thank you, Jenny, and best of luck in the future!
