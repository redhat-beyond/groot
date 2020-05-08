Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "deploy_flask.sh"
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.network :forwarded_port, guest: 5432, host: 1234
  config.vm.provider "virtualbox" do |v|
	v.name ="groot"
	v.memory = 2048
	v.cpus = 4
  end
end