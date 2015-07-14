from pytraj import io as mdio
from pytraj import Trajout

traj = mdio.load("../tests/data/md1_prod.Tc5b.x", "../tests/data/Tc5b.top")[:]
# get x coord of 0-th atom of 0-th frame
print(traj[0, 0, 0])

# get new array with shape = (traj.n_frames, n_atoms, 3)
print(traj[:, :, :].shape)

# get new array with shape (n_atoms, 3) for 0-th frame
print(traj[0, :, :].shape)

# get new Trajectory object with strip atoms
# keeping only CA atoms
print (traj['@CA :frame'])

# get coordinate of all CA atoms for all frames?
# don't use `:frame`
print (traj['@CA'].shape)
# result: (10, 20, 3)