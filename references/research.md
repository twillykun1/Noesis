# 研究线索与设计外推

以下是本项目设计参考，不是对该 skill 效果的直接验证。链接为原始论文、作者资料或官方工程指南。

## 理解成本
- Chandler & Sweller (1991), Cognitive Load Theory and the Format of Instruction. https://doi.org/10.1207/s1532690xci0804_2
  相互依赖的信息分散时增加整合负担。应用推论：把事件、证据、影响和建议相邻呈现。研究场景是教学材料，不能直接断言工程看板提升效率。
- Zhang & Norman (1994), Representations in Distributed Cognitive Tasks. https://pages.ucsd.edu/~scoulson/203/zhang.pdf
  外部表征会改变任务所需的认知操作。推论：让目标/当前决定/未决问题可查看，而非要求用户回忆长对话。
- Rozenblit & Keil (2002), The misunderstood limits of folk science. https://pmc.ncbi.nlm.nih.gov/articles/PMC3062901/
  人会高估对复杂机制的解释深度。推论：不能把“听懂了”当客观理解；这不是故意增加阅读难度或审问用户的依据。

## 人机决策
- Buçinca et al. (2021), To Trust or to Think. https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf
  部分强制思考干预减少错误建议依赖，但带来体验负担，并非所有任务指标改善。不能推导“摩擦越多越好”。
- Vasconcelos et al. (2023), Explanations Can Reduce Overreliance on AI Systems During Decision-Making. https://cicl.stanford.edu/papers/vasconcelos2023explanations.pdf
  多项模拟任务研究强调核验成本与激励。推论：让建议容易核验，不能只增加说服性解释。
- Kazemitabaar et al. (2024), Improving Steering and Verification in AI-Assisted Data Analysis with Interactive Task Decomposition. https://arxiv.org/abs/2407.02651
  小样本数据分析任务的可编辑假设和分步交互研究。支持探索可干预结构，不证明通用开发看板已有效。

## 工程记录
- Michael Nygard, Documenting Architecture Decisions (2011). https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
  记录上下文、决定、状态、后果，保留被取代的理由。这是实践方法，不是因果效果实验。
- Google Engineering Practices: CL Descriptions. https://google.github.io/eng-practices/review/developer/cl-descriptions.html
  解释改动是什么、为什么和必要背景，不只列文件。
- Google Engineering Practices: What to look for in a code review. https://google.github.io/eng-practices/review/reviewer/looking-for.html
  审查设计、功能、复杂性和测试。skill 不替代真实代码评审。

## 尚未证明
该 skill 的整体组合、展示人的影响能否提高其能力、多模型相对单模型的收益、各领域通用性、长期效果，均需额外评测。不能将相关研究或模型共识写成“科学证明本项目有效”。
