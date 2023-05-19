# OOPbeauty
This is my python bot project. I am going to get excellent mark for this task (I hope so)

Ця програма реалізовує примітивного чат бота, який може відповідати на питання у заданих темах
------------------------------------------------------------------------------------------------------

Теми та питання заздалегіть задані для бота. Для того, щоб додати нову тему треба:

  Створити клас теми, унаслідовавши його від абстрактного класу Strategy.
  Потім додати назву теми та об'єкт цього класа у словник, що створюється при 
  ініціалізації класу СhatBot: 
  
  self.strategies = {
  
            "математика": MathStrategy(),
            "фізика": PhysicsStrategy(),
            "географія": GeographyStrategy(),
            "робота з текстом": TextManipulationStrategy(),
            "загальні": GeneralStrategy(),
            "філологія": PhilologyStrategy()
            "ваша нова тема": classObj() - додана нова тема.
            
        } 
        
Для того, щоб додати питання до цієї теми, необхідно:
  Створити унаслідуваний клас з класу теми, а потім 
  додати назву питання до словника sub_str у методі def handle_question(self, question).
