# DECISIONS.md

## Por que análise de sentimento por regras (e não ML)?
- O Neste projeto, a ideia foi optar por uma análise de sentimento baseada em regras simples, em vez de usar um modelo de machine learning. Essa escolha faz sentido porque o foco aqui é ter um protótipo rápido, funcional e fácil de entender.

Com regras, o processo fica mais transparente: dá para ver claramente quais palavras ou expressões estão sendo consideradas positivas, negativas ou neutras. Isso ajuda bastante na hora de explicar o funcionamento e também facilita ajustes, já que basta incluir ou remover termos sem precisar treinar nada de novo.

Outra questão é que trabalhar com machine learning exigiria mais dados rotulados, tempo e recursos, o que foge do objetivo de manter o projeto ágil e enxuto. Para o que foi proposto, as regras já cumprem bem o papel de indicar tendências no que está sendo dito sobre o tema.

Isso não significa que machine learning está descartado. Pelo contrário: conforme o projeto evoluir e houver mais dados disponíveis, faz todo sentido pensar em modelos mais sofisticados. Mas, para este momento, a simplicidade e clareza da abordagem por regras são mais vantajosas.
