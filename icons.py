

XX = (0, 0, 0)
W0 = (255, 255, 255)
W1 = (200, 200, 200)
W2 = (100, 100, 100)

P0 = (255, 20, 140)
P1 = (150, 5, 8)
P2 = (50, 0, 20)

R0 = (255, 0, 0)
R1 = (150, 0, 0)
R2 = (50, 0, 0)

G0 = (0, 255, 0)
G1 = (0, 150, 0)
G2 = (0, 50, 0)

B0 = (0, 0, 255)
B1 = (0, 0, 150)
B2 = (0, 0, 50)


def px_choice(pixel_a, pixel_b):
    '''
    Selects pixel b in priority
    '''
    if pixel_b == XX:
        return pixel_a
    else:
        return pixel_b


def compose_img(image_a, image_b):
    return [px_choice(pixel_a, pixel_b) for pixel_a, pixel_b in zip(image_a, image_b)]


crossed_W0 = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    W0, XX, XX, XX, XX, XX, XX, XX,
    XX, W0, XX, XX, XX, XX, XX, XX,
    XX, XX, W0, XX, XX, XX, XX, XX,
    XX, XX, XX, W0, XX, XX, XX, XX,
    XX, XX, XX, XX, W0, XX, XX, XX,
    XX, XX, XX, XX, XX, W0, XX, XX,
    XX, XX, XX, XX, XX, XX, W0, XX,
]

crossed_W1 = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    W1, XX, XX, XX, XX, XX, XX, XX,
    XX, W1, XX, XX, XX, XX, XX, XX,
    XX, XX, W1, XX, XX, XX, XX, XX,
    XX, XX, XX, W1, XX, XX, XX, XX,
    XX, XX, XX, XX, W1, XX, XX, XX,
    XX, XX, XX, XX, XX, W1, XX, XX,
    XX, XX, XX, XX, XX, XX, W1, XX,
]

crossed_W2 = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    W2, XX, XX, XX, XX, XX, XX, XX,
    XX, W2, XX, XX, XX, XX, XX, XX,
    XX, XX, W2, XX, XX, XX, XX, XX,
    XX, XX, XX, W2, XX, XX, XX, XX,
    XX, XX, XX, XX, W2, XX, XX, XX,
    XX, XX, XX, XX, XX, W2, XX, XX,
    XX, XX, XX, XX, XX, XX, W2, XX,
]

pink_heart = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, P0, P0, XX, P0, P1, XX, XX,
    P0, P0, P0, P1, P1, P1, P1, XX,
    P0, P0, P1, P1, P1, P1, P2, XX,
    XX, P1, P1, P1, P1, P2, XX, XX,
    XX, XX, P1, P1, P2, XX, XX, XX,
    XX, XX, XX, P2, XX, XX, XX, XX,
]

pink_heart_crossed = compose_img(pink_heart, crossed_W1)

pink_heart_empty = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, P0, P0, XX, P0, P1, XX, XX,
    P0, XX, XX, P1, XX, XX, P1, XX,
    P0, XX, XX, XX, XX, XX, P2, XX,
    XX, P1, XX, XX, XX, P2, XX, XX,
    XX, XX, P1, XX, P2, XX, XX, XX,
    XX, XX, XX, P2, XX, XX, XX, XX,
]

pink_heart_empty_crossed = compose_img(pink_heart_empty, crossed_W1)

red_heart = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, R0, R0, XX, R0, R1, XX, XX,
    R0, R0, R0, R0, R1, R1, R1, XX,
    R0, R0, R0, R1, R1, R1, R2, XX,
    XX, R0, R1, R1, R1, R2, XX, XX,
    XX, XX, R1, R1, R2, XX, XX, XX,
    XX, XX, XX, R2, XX, XX, XX, XX,
]

red_heart_crossed = compose_img(red_heart, crossed_W2)

red_heart_empty = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, R0, R0, XX, R0, R1, XX, XX,
    R0, XX, XX, R0, XX, XX, R1, XX,
    R0, XX, XX, XX, XX, XX, R2, XX,
    XX, R0, XX, XX, XX, R2, XX, XX,
    XX, XX, R1, XX, R2, XX, XX, XX,
    XX, XX, XX, R2, XX, XX, XX, XX,
]

red_heart_empty_crossed = compose_img(red_heart_empty, crossed_W2)

fantom_red_tl = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, R0, R0, R0, R1, XX, XX,
    XX, R0, R0, R0, R0, R0, R1, XX,
    R0, R0, XX, W0, R0, XX, W1, R2,
    R0, R0, W0, W0, R0, W1, W1, R2,
    R0, R0, R0, R0, R0, R0, R1, R2,
    R0, R0, R0, R0, R0, R0, R1, R2,
    R0, XX, R0, R0, XX, R0, R1, R2,
]

fantom_red_tr = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, R0, R0, R0, R1, XX, XX,
    XX, R0, R0, R0, R0, R0, R1, XX,
    R0, R0, W0, XX, R0, W1, XX, R2,
    R0, R0, W0, W0, R0, W1, W1, R2,
    R0, R0, R0, R0, R0, R0, R1, R2,
    R0, R0, R0, R0, R0, R0, R1, R2,
    R0, XX, R0, R0, XX, R0, R1, R2,
]

fantom_blue_tl = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, B0, B0, B0, B1, XX, XX,
    XX, B0, B0, B0, B0, B0, B1, XX,
    B0, B0, XX, W0, B0, XX, W1, B2,
    B0, B0, W0, W0, B0, W1, W1, B2,
    B0, B0, B0, B0, B0, B0, B1, B2,
    B0, B0, B0, B0, B0, B0, B1, B2,
    B0, XX, B0, B0, XX, B0, B1, B2,
]

fantom_blue_md = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    XX, XX, B0, B0, B0, B1, XX, XX,
    XX, B0, B0, B0, B0, B0, B1, XX,
    B0, B0, W0, W0, B0, W1, W1, B2,
    B0, B0, W0, XX, B0, XX, W1, B2,
    B0, B0, B0, B0, B0, B0, B1, B2,
    B0, B0, B0, B0, B0, B0, B1, B2,
    B0, XX, B0, B0, XX, B0, B1, B2,
]

skull = [
    XX, W0, W0, W0, W0, W0, W0, XX,
    W0, W0, W0, W0, W0, W0, W0, W0,
    W0, XX, W0, W0, W0, XX, W0, W0,
    W0, R0, W0, W0, W0, R0, W0, W0,
    W0, W0, W0, XX, W0, W0, W0, W0,
    W0, W0, W0, W0, W0, W0, W0, XX,
    XX, W0, XX, W0, XX, W0, XX, XX,
    XX, W2, XX, W2, XX, W2, XX, XX,
]

skull_front = [
    XX, W2, W0, W0, W0, W0, W2, XX,
    W2, W0, W0, W0, W0, W0, W0, W2,
    W0, W0, W0, W0, W0, W0, W0, W0,
    W2, XX, XX, W0, W0, XX, XX, W2,
    W2, XX, R0, W0, W0, R0, XX, W2,
    W0, W0, W0, XX, XX, W0, W0, W0,
    XX, W0, W0, W0, W0, W0, W0, XX,
    XX, W0, XX, W0, W0, XX, W0, XX,
]

skull_front_red = [
    XX, R2, R0, R0, R0, R0, R2, XX,
    R2, R0, R0, R0, R0, R0, R0, R2,
    R0, R0, R0, R0, R0, R0, R0, R0,
    R2, XX, XX, R0, R0, XX, XX, R2,
    R2, XX, W0, R0, R0, W0, XX, R2,
    R0, R0, R0, XX, XX, R0, R0, R0,
    XX, R0, R0, R0, R0, R0, R0, XX,
    XX, R0, XX, R0, R0, XX, R0, XX,
]

demon = [
    XX, XX, XX, XX, XX, XX, XX, XX,
    R0, XX, XX, XX, XX, XX, XX, R0,
    R0, R0, XX, XX, XX, XX, R0, R0,
    XX, R0, XX, XX, XX, XX, R0, XX,
    XX, XX, XX, XX, XX, XX, XX, XX,
    R0, XX, XX, R2, R2, XX, XX, R0,
    XX, R0, R0, R0, R0, R0, R0, XX,
    XX, XX, R0, XX, XX, R0, XX, XX,
]
