import torch
import torch.nn as nn
import torchvision.utils as vutils

# Size of z latent vector (i.e. size of generator input)
NZ = 100

# Size of feature maps in generator
NGF = 64

# Number of GPUs available. Use 0 for CPU mode.
NGPU = 0

# Number of channels in the training images. For color images this is 3
NC = 3


class Generator(nn.Module):
    """DCGAN Generator model

    Args:
        nn (_type_): nn modules
    """

    def __init__(self, ngpu):
        super(Generator, self).__init__()
        self.ngpu = ngpu
        self.main = nn.Sequential(
            # input is Z, going into a convolution
            nn.ConvTranspose2d(NZ, NGF * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(NGF * 8),
            nn.ReLU(True),
            # state size. (NGF*8) x 4 x 4
            nn.ConvTranspose2d(NGF * 8, NGF * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(NGF * 4),
            nn.ReLU(True),
            # state size. (NGF*4) x 8 x 8
            nn.ConvTranspose2d(NGF * 4, NGF * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(NGF * 2),
            nn.ReLU(True),
            # state size. (NGF*2) x 16 x 16
            nn.ConvTranspose2d(NGF * 2, NGF, 4, 2, 1, bias=False),
            nn.BatchNorm2d(NGF),
            nn.ReLU(True),
            # state size. (NGF) x 32 x 32
            nn.ConvTranspose2d(NGF, NC, 4, 2, 1, bias=False),
            nn.Tanh()
            # state size. (nc) x 64 x 64
        )

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return self.main(input)


model = Generator(NGPU)
model.load_state_dict(torch.load("models/flowers_1000.pth"))
model.eval()


@torch.no_grad()
def image():
    """Return image from model"""

    input = torch.randn(1, 100, 1, 1, device="cpu")
    fake = model(input)

    vutils.save_image(
        vutils.make_grid(fake[0], padding=2, normalize=True),
        "./output/image_" + ".png",
    )
