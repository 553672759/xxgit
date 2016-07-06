import java.awt.*;
import java.awt.event.*;
import java.io.IOException;
import java.net.*;
import java.io.*;

public class ChatClient extends Frame{//包装类
	
	TextField tfTxt=new TextField();
	TextArea taContent=new TextArea();
	Socket s;
	DataOutputStream dos=null;
	DataInputStream dis=null;
	private boolean bConnected=false;
	Thread tRecv=new Thread(new RecvThread());
	
	public static void main(String[] args) {
		new ChatClient().launchFrame();
		
	}
	
	//创建窗口
	public void launchFrame(){
		setLocation(400,300);
		this.setSize(300,300);
		add(tfTxt,BorderLayout.SOUTH);
		add(taContent,BorderLayout.NORTH);
		pack();
		this.addWindowListener(new WindowAdapter(){

			@Override
			public void windowClosing(WindowEvent e) {
				disconnect();
				System.exit(0);
			}
			
		});
		tfTxt.addActionListener(new TfListener());
		setVisible(true);
		connect();
		tRecv.start();
	}
	
	//创建连接
	public void connect(){
		try {
			 s=new Socket("127.0.0.1",8888);
			 dos=new DataOutputStream(s.getOutputStream());
			 dis=new DataInputStream(s.getInputStream());
System.out.println("connected!");
			bConnected=true;
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	//关闭流方法
	public void disconnect(){
		
			try {
				dos.close();
				dis.close();
				s.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
			
			/*
			 * 合并线程，关闭线程，如果堵塞程序，设置线程等待一段时间，还没相应，直接关闭
			 */
			
		
	}
	//用于监听回车的内部类
	private class TfListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			String str=tfTxt.getText().trim();
			//taContent.setText(str);
			tfTxt.setText("");
			try {
				dos.writeUTF(str);
				dos.flush();
				//dos.close();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}
		
	}
	
	private class RecvThread implements Runnable{

		@Override
		public void run() {
			while(bConnected){
				String str;
				try {
					str = dis.readUTF();
					taContent.setText(taContent.getText()+str+"\n");
					System.out.println(str);
				}catch(SocketException e){
						System.out.println("退出了");				
				}catch(EOFException e){
					System.out.println("exit!");
				}
					catch (IOException e) {
					e.printStackTrace();
				}
				
			}
		}
		
	}
}







