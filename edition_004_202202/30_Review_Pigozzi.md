# Review: Interactions Between Learning and Evolution (Ackley and Littman, 1991)

*By Federico Pigozzi, University of Trieste (pigozzife@gmail.com)*

Link: https://www.gwern.net/docs/reinforcement-learning/1992-ackley.pdf

The authors experiment with a grid-world environment, which rewards agents for eating food and punishes them for dying (either of starvation or being killed by predators). The agent model employs two networks: an evaluation network that predicts the goodness of a state, and an action network that selects the next action. A genetic algorithm evolves the evaluation network against a “survival” fitness function, while a temporal reinforcement learning algorithm learns the action network (over the course of a simulation), using the output of the evaluation network as reward.

The main result is that learning and evolution together were more successful than either alone in producing adaptive populations; the authors attributed the result to the Baldwin effect, by which agents used learning to stay alive while waiting for successful behaviours to be incorporated directly into the genetic code in the form of preferences.

Moreover, the authors found that successful inherited behaviours “shielded” the inherited preferences, allowing for deleterious mutations to accumulate and eventually leading to maladaptations and instability in the population dynamics. While the former result had already been witnessed in simulations, the latter revealed a novelty.

Reason why I liked it: (Effective) adaptation in animals emerges from the interplay between evolved, instinctive traits (e.g., body) and learned, plastic traits (e.g., behaviour). Starting from the seminal study of Hinton and Nowlan (1987), researchers have asked themselves how learning and evolution can extend each other. As a matter of example, we have recently witnessed a surge in robotics papers attempting to learn controllers while evolving morphologies, and it looks a very promising research direction for the future.
