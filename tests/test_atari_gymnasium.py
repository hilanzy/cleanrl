import subprocess


def test_dqn():
    subprocess.run(
        "python cleanrl/dqn_atari.py --learning-starts 10 --total-timesteps 16 --buffer-size 10 --batch-size 4",
        shell=True,
        check=True,
    )


def test_dqn_eval():
    subprocess.run(
        "python cleanrl/dqn_atari.py --save-model True --learning-starts 10 --total-timesteps 16 --buffer-size 10 --batch-size 4",
        shell=True,
        check=True,
    )


def test_qdagger_dqn_atari_impalacnn():
    subprocess.run(
        "python cleanrl/qdagger_dqn_atari_impalacnn.py --learning-starts 10 --total-timesteps 16 --buffer-size 10 --batch-size 4 --teacher-steps 16 --offline-steps 16 --teacher-eval-episodes 1",
        shell=True,
        check=True,
    )


def test_qdagger_dqn_atari_impalacnn_eval():
    subprocess.run(
        "python cleanrl/qdagger_dqn_atari_impalacnn.py --save-model True --learning-starts 10 --total-timesteps 16 --buffer-size 10 --batch-size 4 --teacher-steps 16 --offline-steps 16 --teacher-eval-episodes 1",
        shell=True,
        check=True,
    )
