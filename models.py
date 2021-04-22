from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Currency
)
import random


author = 'Curtis Kephart (economicurtis@gmail.com)'

doc = """
Real Effort Task. Type as many strings as possible.  
"""

class Constants(BaseConstants):
    name_in_url = 'sabotage'
    players_per_group = None
    task_timer = 120 #see Subsession, before_session_starts setting.
    num_rounds = 50 # must be more than the max one person can do in task_timer seconds
    tournament_rate= 100
    sabotage_endowment = 50
    sabotage_increment = 1
    cost_of_sabotage_per_unit = 10
    sabotage_choices = currency_range(0, sabotage_endowment, sabotage_increment)


    reference_texts = [
        'uIzR',
        'o8sA',
        'dWg5',
        '6kdA',
        'ep7o',
        'zflY',
        'CwNg',
        'OhZn',
        'Xw0w',
        'GJcR',
        'OJ2D',
        'kJ03',
        'L5O8',
        '1MUj',
        'GleS',
        '4gKx',
        'mSol',
        'oWKd',
        'OFFz',
        'CdsT',
        'Mf4U',
        'sUhJ',
        '1Ltw',
        '2mrm',
        'f5UI',
        'hNqN',
        'boJa',
        '2Pqv',
        'vLuq',
        'IYYP',
        'sy3O',
        'M9X6',
        'qflm',
        'ovAU',
        '7PaW',
        'YB4F',
        '2NFP',
        'h6QM',
        'xLkH',
        'izif',
        'r7Ml',
        'ERJ8',
        'geTe',
        'L15N',
        'uTKl',
        'wRuQ',
        'MFNc',
        'YS4B',
        '80uw',
        'syXc',
    ]

    # 'hNqN',
    # 'boJa',
    # '2Pqv',
    # 'vLuq',
    # 'IYYP',

    answer_key1 = [
        'uIzR',
        'o8sA',
        'dWg5',
        '6kdA',
        'ep7o',
        'zflY',
        'CwNg',
        'OhZn',
        'Xw0w',
        'GJcR',
        'OJ2D',
        'kJ03',
        'L5O8',
        '1MUj',
        'GleS',
        '4gKx',
        'mSol',
        'oWKd',
        'OFFz',
        'CdsT',
        '4gKx',
        'mSol',
        'oWKd',
        'OFFz',
        'CdsT',
        'Mf4U',
        'sUhJ',
        '1Ltw',
        '2mrm',
        'f5UI',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
    ]

    answer_key2 = [
        'uIzR',
        'o8sA',
        'dWg5',
        '6kdA',
        'ep7o',
        'zflY',
        'CwNg',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
    ]

    answer_key3 = [
        'uIzR',
        'o8sA',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx',
    ]


    # 'sy3O',
    # 'M9X6',
    # 'qflm',
    # 'ovAU',
    # '7PaW',
    # 'YB4F',
    # '2NFP',
    # 'h6QM',
    # 'xLkH',
    # 'izif',
    # 'r7Ml',
    # 'ERJ8',
    # 'geTe',
    # 'L15N',
    # 'uTKl',
    # 'wRuQ',
    # 'MFNc',
    # 'YS4B',
    # '80uw',
    # 'syXc',
    # 'QgvI',
    # 'a5bk',
    # 'MqCQ',
    # 'E0Qi',
    # 'NzsZ',
    # '1maT',
    # 'mN28',
    # 'BJet',
    # 'xBhz',
    # 'rkn7',
    # '5r3d',
    # 'uTM0',
    # 'pYQD',
    # 'Rkn1',
    # 'FJIv',
    # 'pZMh',
    # 'GobN',
    # 'oVis',
    # '3V4w',
    # 'zWtd',
    # '5OZz',
    # 'ArfP',
    # 'IdzS',
    # 'mC9T',
    # '7cIv',
    # 'TjcG',
    # 'fZ15',
    # 'NlsB',
    # 'tPX4',
    # '3O3c',
    # 'HLTg',
    # 'de14',
    # 'MbqN',
    # 'xywd',
    # 'Z3Vz',
    # 'XS7V',
    # 'ErGB',
    # 'HlTl',
    # '9Dmt',
    # 'LCwT',
    # 'y97e',
    # '6PTp',
    # 'vCVC',
    # 'MG3S',
    # 'kzpF',
    # 'Y90ZQ4gFs287',
    # 'WSx7IJ8YMeAF',
    # '6gt6k1dZfDdL',
    # '8gkmGZY36lBI',
    # 'tz4hJ6NVBPBq',
    # 'SY3BOD92q0Uc',
    # 'FAojzXfsCvsc',
    # '7Hoep0BQ5EgX',
    # 'TXVUwqGND0Hw',
    # 'Ig6hl84vsv05',
    # 'Lk5bKpQ13kTv',
    # 'bRsi7Cbd4gPs',
    # 'jY3X0XKXib1R',
    # 'e3Hs759fdegV',
    # 'NMtMkEyyyly3',
    # 'O2lG0j7cMaRk',
    # 'rkegxeTnoxM8',
    # 'Cs7Yn0FOgqFi',
    # 'GpZTwpsLUq0h',
    # 'EJB4YDNxKcQV',
    # 'zRAyc20FFGiM',
    # 'GSyitZNp3aCa',
    # 'fZPnL4W4Rk8U',
    # 'Cuw7jF0ERvtk',
    # '7JAOg5tGMBic',
    # 'BXVXpjlFuIl6',
    # '7zQTu9YeU0hn',
    # 'M8XxBg30iMjq',
    # 'Bv4jsM4PphLB',
    # '3wdvp9cQMEKU',
    # 'V4x7BM8oqpMN',

class Subsession(BaseSubsession):

    # number_of_males = models.IntegerField()
        # for p in self.session.get_participants():
        #     p.num_males_in_department1 = sum(p.vars['male'])
        # for p in self.get_players():
        #     if p.participant.vars['male'] is not None and p.participant.vars['department'] == 1:
        #         p.num_males_in_department1 = sum(p.participant.vars['male'])

    def creating_session(self):

        #self.session.number_of_males = sum(p.vars['male'] for p in self.session.get_participants())
        # self.session.number_of_males = sum(p.participant.vars['male'] for p in self.get_players())
        # print("Percentage of males in the session:", self.session.number_of_males)

        players = self.get_players()
        if 'task_timer' in self.session.config:
            task_timer = self.session.config['task_timer']
        else:
            task_timer = Constants.task_timer

        for p in self.get_players():
            p.task_timer = task_timer
            p.correct_text = Constants.reference_texts[self.round_number - 1]

        # if self.round_number == 1:
        #     self.group_randomly()
        # else:
        #     self.group_like_round(1)

class Group(BaseGroup):

    winning_performance = models.FloatField()
    losing_performance = models.FloatField()

    other_avatar1 = models.IntegerField()
    other_avatar2 = models.IntegerField()

    paying_period = models.StringField()

    random_period = models.IntegerField()
    sabotage_chosen = models.IntegerField()

    random_sabotage_player = models.IntegerField()

    def set_ranks_before_sabotage(self):

        players = self.get_players()
        for p in players:
            p.total_correct = sum([p.payoff_score for p in p.in_all_rounds()])
            print("Player:", p.id_in_group, " total number of correct answers is", p.total_correct)

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p1.total_correct >= p2.total_correct:
            p1.rank_before_sabotage = 1
            p2.rank_before_sabotage = 2
        else:
            p1.rank_before_sabotage = 2
            p2.rank_before_sabotage = 1

        players = self.get_players()
        for p in players:
            if p.rank_before_sabotage == 1:
                p.rank_before_sabotage_str = 'Birinci'
            elif p.rank_before_sabotage == 2:
                p.rank_before_sabotage_str = 'İkinci'

            p.participant.vars['rank_str'] = p.rank_before_sabotage_str
            print("Player:", p.id_in_group, "rank before sabotage ", p.rank_before_sabotage, p.rank_before_sabotage_str)

    def set_payoffs_after_sabotage(self):

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        # Without feedback
        p1.total_correct_after_sabotage = p1.total_correct-p2.sabotage/Constants.cost_of_sabotage_per_unit
        p2.total_correct_after_sabotage = p2.total_correct - p1.sabotage / Constants.cost_of_sabotage_per_unit

        if p1.total_correct_after_sabotage >= p2.total_correct_after_sabotage:
            p1.payoff_sabotage = Constants.tournament_rate
            p1.rank_after_sabotage = 1

            p2.payoff_sabotage = 0
            p2.rank_after_sabotage = 1
        else:
            p2.payoff_sabotage = Constants.tournament_rate
            p2.rank_after_sabotage = 1

            p1.payoff_sabotage = 0
            p1.rank_after_sabotage = 2

        for p in self.get_players():
            p.participant.vars['payoff_sabotage'] = p.payoff_sabotage
            print('Payoff Sabotage (participant var):', p.participant.vars['payoff_sabotage'])


        # # With feedback
        # p1.total_correct_after_feedback = p1.total_correct-p2.sabotage_post/Constants.cost_of_sabotage_per_unit
        # p2.total_correct_after_feedback = p2.total_correct - p1.sabotage_post / Constants.cost_of_sabotage_per_unit
        #
        # if p1.total_correct_after_feedback >= p2.total_correct_after_feedback:
        #     p1.payoff_after_feedback = Constants.tournament_rate
        #     p1.rank_after_feedback = 1
        #
        #     p2.payoff_after_feedback = 0
        #     p2.rank_after_feedback = 2
        #
        # else:
        #     p2.payoff_sabotage_after_feedback = Constants.tournament_rate
        #     p2.rank_sabotage_after_feedback = 1
        #
        #     p1.payoff_sabotage_after_feedback = 0
        #     p1.rank_sabotage_after_feedback = 2
        #
        # paying_period = random.randint(1, 2)
        # players = self.get_players()
        # for p in players:
        #     if paying_period == 1:
        #         self.paying_period = 'Sabotage without feedback'
        #         p.payoff_sabotage = p.payoff_after_sabotage
        #
        #     elif paying_period == 2:
        #         self.paying_period = 'Sabotage with feedback'
        #         p.payoff_sabotage = p.payoff_after_feedback

        players = self.get_players()
        for p in players:
            print('Player', p.id_in_group, 'total correct after sabotage', p.total_correct_after_sabotage)

    def set_belief_payoffs(self):

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        diff_p1 = p1.sabotage_belief - p2.sabotage
        diff_p2 = p2.sabotage_belief - p1.sabotage

        if -10 <= diff_p1 <= 10:
            p1.payoff_belief = 10
        else:
            p1.payoff_belief = 0

        if -10 <= diff_p2 <= 10:
            p2.payoff_belief = 5
        else:
            p2.payoff_belief = 0

        print('Player 1', p1.id_in_group, 'payoff from belief: ', p1.payoff_belief)
        print('Player 2', p2.id_in_group, 'payoff from belief: ', p2.payoff_belief)


        players = self.get_players()
        for p in players:
            p.payoff_sabotage = p.payoff_sabotage + p.payoff_belief


class Player(BasePlayer):

    rank_before_sabotage = models.IntegerField()
    rank_after_sabotage = models.IntegerField()
    rank_after_feedback = models.IntegerField()

    rank_before_sabotage_str = models.StringField()

    payoff_before_sabotage = models.IntegerField()
    payoff_after_sabotage = models.IntegerField()
    payoff_after_feedback = models.IntegerField()

    payoff_sabotage = models.IntegerField(initial=0)
    payoff_belief = models.IntegerField(initial=0)

    total_correct_after_sabotage = models.FloatField(initial=0)
    total_correct_after_feedback = models.FloatField(initial=0)
    total_correct = models.FloatField(initial=0)

    # sabotage = models.IntegerField(
    #     choices=[
    #         [0, '0'],
    #         [5, '5'],
    #         [10, '10'],
    #         [15, '15'],
    #         [20, '20'],
    #         [25, '25'],
    #     ],
    #     widget=widgets.RadioSelect,
    #     label=""
    # )

    # sabotage_belief = models.IntegerField(
    #     choices=[
    #         [0, '0'],
    #         [5, '5'],
    #         [10, '10'],
    #         [15, '15'],
    #         [20, '20'],
    #         [25, '25'],
    #     ],
    #     widget=widgets.RadioSelect,
    #     label=""
    # )

    sabotage = models.IntegerField(min=0, max=50, label="Lütfen diğer oyuncudan kaç TL değerinde doğru eksiltmek istediğizi seçiniz. (Lütfen boşluğa 0 ile 50 arasında bir sayı giriniz)")
    sabotage_belief = models.IntegerField(min=0, max=50, label="")
    sabotage_post = models.IntegerField(min=0, max=50, label="Lütfen diğer oyuncudan kaç TL değerinde doğru eksiltmek istediğizi seçiniz. (Lütfen boşluğa 0 ile 50 arasında bir sayı giriniz)")

    belief = models.IntegerField(
        choices=[
            [1, 'Birinci'],
            [2, 'İkinci'],
        ],
        widget=widgets.RadioSelect,
        label=""
    )

    task_timer = models.PositiveIntegerField(
        doc="""The length of the real effort task timer."""
    )

    correct_text = models.CharField(
        doc="user's transcribed text")

    user_text = models.CharField(
        doc="user's transcribed text",
        widget=widgets.TextInput(attrs={'autocomplete':'off'}))

    is_correct = models.BooleanField(
        doc="did the user get the task correct?")

    ret_final_score = models.IntegerField(
        doc="player's total score up to this round")

    payoff_score = models.IntegerField(initial=0, doc = '''score in this task''')

    is_winner = models.BooleanField()

    rank = models.IntegerField()
    rank_str = models.StringField()

    other_male = models.IntegerField(initial=0)
    other_avatar = models.StringField(initial='male')


    #
    # def set_belief_payoffs(self):
    #
    #     if self.rank == self.belief:
    #         self.payoff_belief = 5
    #     else:
    #         self.payoff_belief = 0

    def score_round(self):
        # update player payoffs
        if self.correct_text == self.user_text:
            self.is_correct = True
            self.payoff_score = 1
        else:
            self.is_correct = False
            self.payoff_score = 0
