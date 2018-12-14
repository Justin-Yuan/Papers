### StoryGAN: A Sequential Conditional GAN for Story Visualization
[link](https://arxiv.org/pdf/1812.02784.pdf)

#### Intro 

- given a multi-sentence paragraph, generate a sequence of images,one for each sentence
- story visualizatoin focuses less on the continuity in frames, but more on the global consistency across dynamic scenes and characters 
- Text2Gist component, the sentence description is transformed into a filter and adapted to the story, optimize the mixing process by tweakign the filter 
- two-level GAN, image-level discriminator to measure relevance of a sentence and its generated image; story-level discriminator to measure global coherence between generated image and the whole story 
- context encoder, capture contectual informatino during sequential image generation, 2-layer RNN, lower layer uses standard GRU, upper layer uses Text2Gist cells 


<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 




<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 




<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 